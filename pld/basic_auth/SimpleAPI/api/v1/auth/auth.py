#!/usr/bin/env python3
"""auth class"""
from flask import request
from typing import List, TypeVar
from models.user import User

class Auth:
    """auth class"""
    # ------- start of require_auth --------
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """checks if path requires authentication"""
        if path is None or not path:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        path = path if path.endswith('/') else path + '/'
        if path in excluded_paths:
            return False
        return True

    # ----- end of require_auth -----------
    def authorization_header(self, request=None) -> str:
        """checks authorization header"""
        if request is None or request.headers.get("Authorization") is None:
            return None
        return request.headers.get("Authorization")
    
    def current_user(self, request=None) -> TypeVar('User'):
        """for the current user"""
        return None
    