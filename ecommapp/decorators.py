from django.contrib.auth.decorators import user_passes_test

#created decorators so that every user get verified while registering
def verification_required(f):
    return user_passes_test(lambda u: u.is_verified, login_url='/verify')(f)
