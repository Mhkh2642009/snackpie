import sys
import os
import io
import re
import contextlib
import signal
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))


class SnackPieRunner:
    """Runs SnackPie code in a sandboxed environment."""
    
    def __init__(self, timeout=2):
        self.timeout = timeout
    
    def run(self, code: str, stdin_input: str = "") -> dict:
        """
        Execute SnackPie code and capture output.
        
        Args:
            code: SnackPie source code to execute
            stdin_input: Simulated input for 'ask' commands
            
        Returns:
            dict with 'success', 'output', and 'error' keys
        """
        from snackpie import prog, VAR, SAY, ASk, IFstatement, calc
        
        # Reset global state
        VAR.all = {}
        
        # Capture output
        stdout = io.StringIO()
        stderr = io.StringIO()
        
        # Prepare input queue for 'ask' commands
        input_lines = stdin_input.splitlines() if stdin_input else []
        input_iter = iter(input_lines)
        
        def mock_input(prompt=""):
            """Mock input() to use pre-supplied values."""
            try:
                return next(input_iter)
            except StopIteration:
                return ""
        
        original_exit = sys.exit
        
        def mock_exit(code=0):
            if code == 'OUT':
                raise SystemExit('OUT')
            raise SystemExit(code)
        
        try:
            with contextlib.redirect_stdout(stdout), \
                 contextlib.redirect_stderr(stderr), \
                 patch('builtins.input', mock_input), \
                 patch('sys.exit', mock_exit):
                
                # Execute line by line
                for line in code.strip().split('\n'):
                    stripped = line.rstrip()
                    if stripped:
                        try:
                            prog(stripped)
                        except SystemExit:
                            break
            
            return {
                "success": True,
                "output": stdout.getvalue(),
                "error": None
            }
            
        except SystemExit as e:
            error_msg = str(e) if str(e) != 'OUT' else None
            return {
                "success": error_msg is None,
                "output": stdout.getvalue(),
                "error": error_msg
            }
        except Exception as e:
            return {
                "success": False,
                "output": stdout.getvalue(),
                "error": f"{type(e).__name__}: {str(e)}"
            }
        finally:
            # Restore global state
            VAR.all = {}
    
    def validate(self, code: str) -> dict:
        """Check syntax without executing."""
        errors = []
        lines = code.strip().split('\n')
        
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if not stripped:
                continue
            
            # Basic syntax checks
            if stripped.startswith('orif ') and not any(c in stripped for c in ['==', '!=', '>', '<', '>=', '<=']):
                errors.append(f"Line {i}: orif statement missing comparison operator")
            
            if stripped == 'end' and i == 1:
                errors.append(f"Line {i}: unexpected 'end' without matching 'if'")
            
            if stripped.startswith('if ') and not stripped.endswith(':'):
                errors.append(f"Line {i}: if statement must end with ':'")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors
        }
