from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError("이메일이 입력되지 않았어요!")
        normalized_email = self.normalize_email(email)
        user = self.model(
            username=normalized_email,
            email=normalized_email,
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, nickname, password=None):
        user = self.create_user(email=email, password=password, nickname=nickname)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
