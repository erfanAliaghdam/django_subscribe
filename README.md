# django_subscribe


first signup on mailtrp.io and get api key for fake smtp test
or you can use your own smtp server



use this structure for .env file inside root:

jwt token validation in days: 

> ACCESS_TOKEN_LIFETIME_BY_DAYS = 10

jwt refresh token validation :

> REFRESH_TOKEN_LIFETIME_BY_DAYS = 11

db config : 

> ENGINE = 'django.db.backends.postgresql'

> NAME = 'postgres'

> USER = 'postgres'

> PASSWORD = 'postgres'

> HOST = 'postgres'

> PORT = '5432'

secret key, you can use https://djecrety.ir website:

> SECRET_KEY = ''

smtp config : 

> EMAIL_HOST =  'smtp.mailtrap.io'
> EMAIL_HOST_USER = ''
> EMAIL_HOST_PASSWORD = ''
> EMAIL_PORT = '2525'



now you can use command running the project:
> docker-compose up -d --build

access shell and create your own superuser:
> docker-compose run web shell

> ./manage.py createsuperuser

create free plan with command:
> ./manage.py createplanfree

now you can signup a user with this endpoint:
> 127.0.0.1:8000/api/auth/users/

an activation link will send to email click and activate.
now another email for free trial will send to your email, but you should login for subscribe.

get your jwt login with :
> 127.0.0.1:8000/api/auth/jwt/create/

after logging in with jwt you can click on email for trial and subscribe with this instruction:
request type: post
> 127.0.0.1:8000/api/auth/plans/<id>/subscribe/

you can see your subscribed plans list:
> 127.0.0.1:8000/api/auth/plans/me/
