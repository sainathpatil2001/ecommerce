from django.shortcuts import redirect
from functools import wraps
from accounts.models import RigisterdUser
def login_required_custom(view_func):
    """
    Custom decorator to restrict access to views for unauthenticated users.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the 'user_id' is in the session
        user_id = request.session.get('user_id')
        
        if not user_id:
            # Redirect to the login page if user is not logged in
            return redirect('login')  # Replace 'login' with your login URL name
        
        # Optional: Validate session or user ID in database
        
        if not RigisterdUser.objects.filter(id=user_id).exists():
            request.session.flush()  # Clear session
            return redirect('login')
        
        # Proceed to the view if user is authenticated
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view
