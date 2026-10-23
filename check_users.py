import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voting_project.settings')
django.setup()

from accounts.models import User
from django.contrib.auth import authenticate

print("\n" + "="*60)
print("LOGIN DEBUG")
print("="*60 + "\n")

# Check if admin exists
try:
    admin = User.objects.get(username='admin')
    print("✓ Admin user found in database")
    print(f"  Username: {admin.username}")
    print(f"  Email: {admin.email}")
    print(f"  User Type: {admin.user_type}")
    print(f"  Is Superuser: {admin.is_superuser}")
    print(f"  Is Staff: {admin.is_staff}")
    print(f"  Is Active: {admin.is_active}")
    print(f"  Password Hash: {admin.password[:20]}...")
    
    # Test authentication
    print("\n" + "-"*60)
    print("Testing authentication with 'admin123':")
    print("-"*60)
    
    user = authenticate(username='admin', password='admin123')
    
    if user:
        print("✓ Authentication SUCCESSFUL")
        print(f"  Authenticated as: {user.username}")
    else:
        print("✗ Authentication FAILED")
        print("\nTrying to reset password...")
        
        # Reset password
        admin.set_password('admin123')
        admin.save()
        print("✓ Password reset to 'admin123'")
        
        # Test again
        user = authenticate(username='admin', password='admin123')
        if user:
            print("✓ Authentication now works!")
        else:
            print("✗ Still not working - there might be an issue with your User model")
    
except User.DoesNotExist:
    print("✗ Admin user NOT found in database")
    print("\nCreating admin user now...")
    
    try:
        admin = User.objects.create_user(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        admin.user_type = 'superadmin'
        admin.is_superuser = True
        admin.is_staff = True
        admin.is_active = True
        admin.save()
        
        print("✓ Admin created successfully!")
        
        # Test authentication
        user = authenticate(username='admin', password='admin123')
        if user:
            print("✓ Authentication works!")
        else:
            print("✗ Created but authentication failed")
            
    except Exception as e:
        print(f"✗ Error creating admin: {str(e)}")

# List all users
print("\n" + "="*60)
print("ALL USERS IN DATABASE:")
print("="*60)

for user in User.objects.all():
    print(f"\n{user.username}:")
    print(f"  Type: {user.user_type}")
    print(f"  Active: {user.is_active}")
    print(f"  Staff: {user.is_staff}")
    print(f"  Superuser: {user.is_superuser}")

print("\n" + "="*60)
print("TRY LOGGING IN WITH:")
print("="*60)
print("URL: http://127.0.0.1:8000/accounts/login/")
print("Username: admin")
print("Password: admin123")
print("="*60 + "\n")
