def is_valid_email(s):
    return "@" in s and "." in s

!pytest -q
!git add email_check.py
!git commit -m "Fix email verification logic to use and"
!git push
