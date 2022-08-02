# Regex entries

## 1. About

A Django app that let's users store handy regular expressions to lookup against at a later time.

For example - 
* [0-9] - Would match any number between `0` to `9`
* [a-z] - Would match any lower cases alphabet
* [A-Z] - Would match any lower cases alphabet

See https://docs.python.org/3/howto/regex.html#matching-characters for more details.

## 2. Quickstart Django - Setting Things Up

### 2.1 Create project directory

```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/1.models/1.skeleton$>mkdir project-regex
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/1.models/1.skeleton>cd project-regex
```

### 2.2 Pick a version

* Pick an LTS version - https://www.djangoproject.com/download/
* Add into `requirements.txt` - https://pip.pypa.io/en/stable/user_guide/#requirements-files
* And install packages - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/2.admin/2.hook_in_entries_on_admin/project-regex$ pip install -r requirements.txt
Requirement already satisfied: django==3.2.3 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 1)) (3.2.3)
Requirement already satisfied: pycodestyle==2.7.0 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 2)) (2.7.0)
Requirement already satisfied: asgiref<4,>=3.3.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from django==3.2.3->-r requirements.txt (line 1)) (3.3.4)
Requirement already satisfied: sqlparse>=0.2.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from django==3.2.3->-r requirements.txt (line 1)) (0.4.1)
Requirement already satisfied: pytz in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from django==3.2.3->-r requirements.txt (line 1)) (2021.1)
```

### 2.3 Create Django project

* Run command - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/1.models/1.skeleton/project-regex$ django-admin startproject regex
```
* Folder structure looks something like - 
```
- project-regex
    - regex
        - regex
            - asgi.py
            - settings.py
            - urls.py
            - wsgi.py
        - manage.py
```

### 2.4 Run server

* Run server to confirm installation works -
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/1.models/1.skeleton/project-regex/regex$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
June 09, 2021 - 16:15:15
Django version 3.2.3, using settings 'regex.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
* Confirm obligatory welcome page is visible on Chrome - http://localhost:8000/

### 2.5 Create Django app

* Run command - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/1.models/2.add_app/project-regex/regex$ python manage.py startapp entries
```
* Folder structure looks something like - 
```
- project-regex
    - regex
        - db.sqlite3
        - entries
            - migrations
                - (empty)
            - admin.py
            - apps.py
            - models.py
            - tests.py
            - views.py
        - regex
            - asgi.py
            - settings.py
            - urls.py
            - wsgi.py
        - manage.py
```

## 3. Quickstart Django - Models

### 3.1 Deal with unapplied core Django app migrations first

* Note that there are unapplied migrations - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/1.models/3.add_model/project-regex/regex$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
June 09, 2021 - 16:17:19
Django version 3.2.3, using settings 'regex.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
* Run the migrations - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/1.models/3.add_model/project-regex/regex$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```
* Note that unapplied migrations no longer shows up - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/1.models/3.add_model/project-regex/regex$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 09, 2021 - 16:20:31
Django version 3.2.3, using settings 'regex.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### 3.2 Deal with custom app migrations next

* Add the relevant changes into `models.py`
* Try generating the corresponding migrations file, but note that it thinks there is no change - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/1.models/3.add_model/project-regex/regex$ python manage.py makemigrations
No changes detected
```
* Inform Django that a new app is now available, to detect migrations, in `settings.py`
* Try generating the corresponding migrations file again - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/1.models/3.add_model/project-regex/regex$ python manage.py makemigrations
Migrations for 'entries':
  entries/migrations/0001_initial.py
    - Create model Entry
```
* For the curious, to see what SQL is used, not necessary to run explicitly - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/1.models/3.add_model/project-regex/regex$ python manage.py sqlmigrate entries 0001
BEGIN;
--
-- Create model Entry
--
CREATE TABLE "entries_entry" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "date_added" datetime NOT NULL, "pattern" varchar(255) NOT NULL, "test_string" varchar(255) NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "entries_entry_user_id_8eee90b6" ON "entries_entry" ("user_id");
COMMIT;
```
* Lastly, apply the migrations - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/1.models/3.add_model/project-regex/regex$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, entries, sessions
Running migrations:
  Applying entries.0001_initial... OK
```

## 4. Quickstart Django - Admin

### 4.1 Create superuser

* Run command - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/2.admin/1.log_in_on_admin/project-regex/regex$ python manage.py createsuperuser
Username (leave blank to use 'karand'): 
Email address: 
Password: 
Password (again): 
Superuser created successfully.
```
* Confirm logging in on admin page is now possible using above creds - http://localhost:8000/admin

### 4.2 Fiddle with out-of-box controls/interactions

* Create a few users - about 1-2
* Create a few entries - about 2-3
* Notice the following -
    * http://localhost:8000/admin/ - "Entrys" instead of "Entries" :)
    * http://localhost:8000/admin/entries/entry/ - Tabular view not ... useful/descriptive - 
        * Items listed as "Entry object (3)"
        * No columns
        * No filters
        * No search

### 4.3 Polish up controls/interactions

* Address points listed above
* And run migrations - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/2.admin/3.polish_entries_on_admin/project-regex/regex$ python manage.py makemigrations
Migrations for 'entries':
  entries/migrations/0002_alter_entry_options.py
    - Change Meta options on entry
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/2.admin/3.polish_entries_on_admin/project-regex/regex$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, entries, sessions
Running migrations:
  Applying entries.0002_alter_entry_options... OK
```
* More controls listed all here - https://docs.djangoproject.com/en/3.2/ref/contrib/admin/

### 5. Quickstart Django - Querysets

* Now that data is available let's try to query it, by using `shell_plus`.

# 5.1 Install Django Extensions

* Pick a version - https://pypi.org/project/django-extensions/
* Add into `requirements.txt` - https://pip.pypa.io/en/stable/user_guide/#requirements-files
* And install packages - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/2.admin/4.querysets/project-regex$ pip install -r requirements.txt
Requirement already satisfied: django==3.2.3 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 1)) (3.2.3)
Requirement already satisfied: django-extensions==3.1.3 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 2)) (3.1.3)
Requirement already satisfied: pycodestyle==2.7.0 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 3)) (2.7.0)
Requirement already satisfied: sqlparse>=0.2.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from django==3.2.3->-r requirements.txt (line 1)) (0.4.1)
Requirement already satisfied: pytz in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from django==3.2.3->-r requirements.txt (line 1)) (2021.1)
Requirement already satisfied: asgiref<4,>=3.3.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from django==3.2.3->-r requirements.txt (line 1)) (3.3.4)
```
* Inform Django that a new app is now available, to run additional management commands, in `settings.py`

# 5.2 Check Django version

* Run these - 

```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/2.admin/4.querysets/project-regex/regex$ python manage.py shell_plus
# Shell Plus Model Imports
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from entries.models import Entry
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from django.utils import timezone
from django.urls import reverse
from django.db.models import Exists, OuterRef, Subquery
Python 3.9.5 (default, May  5 2021, 02:58:34) 
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
>>> import django
>>> print(django.get_version())
3.2.3
```
* `shell_plus` is convenient compared to default `shell` - Note how models/hooks are auto-imported above.

# 5.3 Querysets

* The ORM is a beautiful thing - abstracts away which DB is used
* In this case, `SQLite` is being used, typically in "real"/"prod" environments a traditional DB (`Postgres`/`MySQL` etc.) is used.

```
# Reading all available rows
>>> Entry.objects.all()
<QuerySet [<Entry: Entry object (1)>, <Entry: Entry object (2)>, <Entry: Entry object (3)>]>

# Reading the first row
>>> Entry.objects.all()[0]
<Entry: Entry object (1)>

# Reading columns on the first row
>>> Entry.objects.all()[0].id
1
>>> Entry.objects.all()[0].test_string
'9'

# Reading rows based on a filter on a column
# Note - that this is *always* a Queryset ... a collection. To be used when uncertain of rows returned.
>>> Entry.objects.filter(pattern='[A-Z]')
<QuerySet [<Entry: Entry object (3)>]>
>>> Entry.objects.filter(pattern='[A-Z]')[0].id
3
>>> Entry.objects.filter(pattern='random')
<QuerySet []>
>>> Entry.objects.filter(pattern='random').exists()
False
>>> Entry.objects.filter(pattern='[A-Z]').exists()
True

# Reading a single row based columns that uniquely identify a row
# Note - that this is *always* a single ORM object, and complains if not found. To be used sure of row returned.
>>> Entry.objects.get(id=3)
<Entry: Entry object (3)>
>>> Entry.objects.get(id=3).id
3
>>> Entry.objects.get(id=10000)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/karand/workspace/training.python/.tpvenv/lib/python3.6/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/karand/workspace/training.python/.tpvenv/lib/python3.6/site-packages/django/db/models/query.py", line 408, in get
    self.model._meta.object_name
entries.models.Entry.DoesNotExist: Entry matching query does not exist.

# Reading rows based on a filter on a column, with field lookups
>>> Entry.objects.filter(pattern__startswith='[')
<QuerySet [<Entry: Entry object (1)>, <Entry: Entry object (2)>, <Entry: Entry object (3)>]>
>>> Entry.objects.filter(pattern__startswith='[').count()
3
>>> Entry.objects.filter(pattern__contains='beast')
<QuerySet []>

# Inserting rows 
>>> entry = Entry(pattern='[a-z][a-z][a-z]',test_string='ace',user=User.objects.get(username='karand'))
>>> entry.save()
>>> Entry.objects.all()
<QuerySet [<Entry: Entry object (1)>, <Entry: Entry object (2)>, <Entry: Entry object (3)>, <Entry: Entry object (4)>]>

# Updating rows 
>>> entry = Entry.objects.get(id=4)
>>> entry.test_string
'ace'
>>> entry.test_string = 'hut'
>>> entry.save()
>>> entry.test_string
'hut'

# Deleting rows 
>>> entry = Entry.objects.get(id=4)
>>> Entry.objects.all()
<QuerySet [<Entry: Entry object (1)>, <Entry: Entry object (2)>, <Entry: Entry object (3)>, <Entry: Entry object (4)>]>
>>> entry.delete()
(1, {'entries.Entry': 1})
>>> Entry.objects.all()
<QuerySet [<Entry: Entry object (1)>, <Entry: Entry object (2)>, <Entry: Entry object (3)>]>
```
* More query hooks listed here - https://docs.djangoproject.com/en/3.2/ref/models/querysets/

### 6. Quickstart Django - Relations

### 6.1 - O2O

* Need - To 'extend' another model in some way. For example, do not want to mess with core Django User model. So additional details can be captured in a separate UserProfile model.

* Run migrations - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/2.admin/5.o2o/project-regex/regex$ python manage.py makemigrations
Migrations for 'entries':
  entries/migrations/0003_userprofile.py
    - Create model UserProfile
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/2.admin/5.o2o/project-regex/regex$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, entries, sessions
Running migrations:
  Applying entries.0003_userprofile... OK
```

* And queries - 
```
# Reading relation
>>> UserProfile.objects.get(id=1)
<UserProfile: UserProfile object (1)>
>>> UserProfile.objects.get(id=1).user
<User: karand>
>>> UserProfile.objects.get(id=1).user.username
'karand'

# Reading reverse relation
>>> User.objects.get(id=1)
<User: karand>
>>> User.objects.get(id=1).userprofile
<UserProfile: UserProfile object (1)>
>>> User.objects.get(id=1).userprofile.nickname
'KD'
```

* Details - 
    * https://docs.djangoproject.com/en/3.2/ref/models/fields/#onetoonefield
    * https://docs.djangoproject.com/en/3.2/topics/db/examples/one_to_one/

### 6.2 - M2M

* Need - To map multiple rows against two models. For example, techncially the same test strings can actually be mapped against multiple patterns, and vice versa.
* This managed by an intermediary table.
* Run migrations - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/2.admin/6.m2m/project-regex/regex$ python manage.py makemigrations
Migrations for 'entries':
  entries/migrations/0004_auto_20210609_1741.py
    - Create model TestString
    - Remove field test_string from entry
    - Add field test_strings to entry
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/2.admin/6.m2m/project-regex/regex$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, entries, sessions
Running migrations:
  Applying entries.0004_auto_20210609_1741... OK
```
* Note that the default multiselect control in admin is a little awkward ... especially if that list increases.

### 6.3 - M2M (better in admin)

* Let's use an autcomplete instead, and make them user-freindly/readable through th widget.
* Run migrations - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/2.admin/7.m2m-better-admin/project-regex/regex$ python manage.py makemigrations
Migrations for 'entries':
  entries/migrations/0005_alter_teststring_string.py
    - Alter field string on teststring
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/2.admin/7.m2m-better-admin/project-regex/regex$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, entries, sessions
Running migrations:
  Applying entries.0005_alter_teststring_string... OK
```

```
# Reading relation
>>> Entry.objects.get(id=1)
<Entry: 1>
>>> Entry.objects.get(id=1).test_strings
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x7f6c28d135c0>
>>> Entry.objects.get(id=1).test_strings.all()
<QuerySet [<TestString: 0>]>
>>> Entry.objects.get(id=1).test_strings.all()[0].string
'0'

# Reading reverse relation
>>> TestString.objects.get(id=1)
<TestString: J>
>>> TestString.objects.get(id=1).entry_set
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x7f6c293ded68>
>>> TestString.objects.get(id=1).entry_set.all()
<QuerySet [<Entry: 3>]>
>>> TestString.objects.get(id=1).entry_set.all()[0].pattern
'[A-Z]'
```

* Details - 
    * https://docs.djangoproject.com/en/3.2/ref/models/fields/#manytomanyfield
    * https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/
    * https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.autocomplete_fields

### 6.4 - O2M

* Need - To map multiple rows of one model against another, but not vice versa. For example, multiple entries are created (and belong) to a user, but they should not be controlled/mapped against another user.
* And for similar reasons let's use autocomplete fields here as well.

```
# Reading relation
>>> Entry.objects.get(id=1)
<Entry: 1>
>>> Entry.objects.get(id=1).user
<User: karand>

# Reading reverse relation
>>> User.objects.get(id=1)
<User: karand>
>>> User.objects.get(id=1).entry_set
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x7f177f0f0048>
>>> User.objects.get(id=1).entry_set.all()
<QuerySet [<Entry: 1>]>
>>> User.objects.get(id=1).entry_set.all()[0].pattern
'[0-9]'
```

* Details - 
    * https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/
    * https://docs.djangoproject.com/en/3.2/ref/models/fields/#foreignkey

## 7. Quickstart Django - Views

### 7.1 Routing

* Let's hook up some custom views, starting with a skeleton like 'Hello World'
* Routing in Django land is managed through `urls.py`
    * Specify one under `regex.urls`
    * And another under `entries.urls`
    * Note splitting up helps avoid lumping everything in a single file
* Note that this should now load - http://localhost:8000/entries/home/

* Details - https://docs.djangoproject.com/en/3.2/topics/http/urls/

### 7.2 Authenticating

* But ... anyone can access these views
* Let's limit this to authenticated users
* Note that hitting http://localhost:8000/entries/home/ > redirects to http://localhost:8000/admin/login/?next=/entries/home/ > and sends back to url based on query param `next`
* Mixins are super useful options to reuse code without necessarily inheriting everything in the world - composition vs inheritance 

* Details - https://docs.djangoproject.com/en/3.2/topics/auth/default/#the-loginrequired-mixin

### 7.3 Templates

* Let's flesh out the templates - add some html/css
* Add reuseable templates
* Add links
* Note that http://localhost:8000/entries/home/ has a set of links, and that the HTML page is styled

* Details - 
    * https://docs.djangoproject.com/en/3.2/topics/templates/
    * https://docs.djangoproject.com/en/3.2/ref/templates/builtins/

### 7.4 Views

* First off there's the display views - 
    * `ListView` - Let's list out all entries - http://localhost:8000/entries/list/
    * `DetailView` - And then an entry's detail (linked from list) - http://localhost:8000/entries/1/detail/
* And then there's the editing views -
    * `FormView` - And lastly an entry's form that can be updated (linked from detail) - http://localhost:8000/entries/3/form/

* Details -
    * https://docs.djangoproject.com/en/3.2/topics/class-based-views/
    * https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-display/#listview
    * https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-display/#detailview
    * https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-editing/
    * https://docs.djangoproject.com/en/3.2/topics/forms/#the-view
    * https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/#django.views.generic.edit.FormView
    * https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/#createview
    * https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/#updateview
    * https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/#deleteview
    * https://docs.djangoproject.com/en/3.2/intro/tutorial01/


## 8. Quickstart Django - API

### 8.1 Setting Things Up

* Pick a version 
    * https://pypi.org/project/djangorestframework/
    * https://www.django-rest-framework.org/community/release-notes/#312x-series
    * https://www.django-rest-framework.org/#requirements
* Add into `requirements.txt`
* And install packages - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/4.apis/1.skeleton/project-regex$ pip install -r requirements.txt
Requirement already satisfied: django==3.2.3 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 1)) (3.2.3)
Requirement already satisfied: django-extensions==3.1.3 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 2)) (3.1.3)
Requirement already satisfied: djangorestframework==3.12.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 3)) (3.12.2)
Requirement already satisfied: pycodestyle==2.7.0 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 4)) (2.7.0)
Requirement already satisfied: asgiref<4,>=3.3.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from django==3.2.3->-r requirements.txt (line 1)) (3.3.4)
Requirement already satisfied: sqlparse>=0.2.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from django==3.2.3->-r requirements.txt (line 1)) (0.4.1)
Requirement already satisfied: pytz in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from django==3.2.3->-r requirements.txt (line 1)) (2021.1)
```
* Create an app - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/4.api/1.skeleton/project-regex/regex$ python manage.py startapp api
```
* Hook in barebones settings / urls / serializers / viewsets
* And check -
    * Remember to terminate session first - http://localhost:8000/admin/logout/
    * And Browesable API (https://www.django-rest-framework.org/topics/browsable-api/) should load - http://localhost:8000/api/entries/

### 8.2 Add in auth

* Hook in `permissions_classes`
* Remember to terminate session first - http://localhost:8000/admin/logout/
* Note http://localhost:8000/api/entries/ complains with `Authentication credentials were not provided.`
* Login http://localhost:8000/admin/ and try http://localhost:8000/api/entries/ again
* But ... no one really uses sessions with APIs, its all REST Clients

### 8.2 Add in auth, but with token

* First add in https://marketplace.visualstudio.com/items?itemName=humao.rest-client&ssr=false#overview
* Note `sample.http`
* Hook in auth app
* Run relevant migrations - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/4.apis/3.auth-with-token/project-regex/regex$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, authtoken, contenttypes, entries, sessions
Running migrations:
  Applying authtoken.0001_initial... OK
  Applying authtoken.0002_auto_20160226_1747... OK
  Applying authtoken.0003_tokenproxy... OK
```
* Create a token for your user - http://localhost:8000/admin/authtoken/tokenproxy/
* And check using `Authorization` header
* Details - https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication

### 8.3 Deal with relations
Details - https://www.django-rest-framework.org/api-guide/relations/#serializer-relations

### 8.4 Control what operations are supported
Details - https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset


## 9. Quickstart Django - Tests

### 9.1 Setting Things Up

* Installs - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/5.tests/1.skeleton/project-regex$ pip install -r requirements.txt
Collecting coverage==5.5
  Downloading coverage-5.5-cp39-cp39-manylinux2010_x86_64.whl (243 kB)
     |████████████████████████████████| 243 kB 1.4 MB/s 
Requirement already satisfied: django==3.2.3 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 2)) (3.2.3)
Requirement already satisfied: django-extensions==3.1.3 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 3)) (3.1.3)
Requirement already satisfied: djangorestframework==3.12.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 4)) (3.12.2)
Requirement already satisfied: pycodestyle==2.7.0 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 5)) (2.7.0)
Collecting pytest==6.2.4
  Downloading pytest-6.2.4-py3-none-any.whl (280 kB)
     |████████████████████████████████| 280 kB 1.9 MB/s 
Collecting pytest-cov==2.12.1
  Downloading pytest_cov-2.12.1-py2.py3-none-any.whl (20 kB)
Collecting pytest-django==4.4.0
  Downloading pytest_django-4.4.0-py3-none-any.whl (19 kB)
Collecting pytest-xdist==2.2.1
  Downloading pytest_xdist-2.2.1-py3-none-any.whl (37 kB)
Requirement already satisfied: sqlparse>=0.2.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from django==3.2.3->-r requirements.txt (line 2)) (0.4.1)
Requirement already satisfied: asgiref<4,>=3.3.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from django==3.2.3->-r requirements.txt (line 2)) (3.3.4)
Requirement already satisfied: pytz in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from django==3.2.3->-r requirements.txt (line 2)) (2021.1)
Requirement already satisfied: packaging in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest==6.2.4->-r requirements.txt (line 6)) (20.9)
Requirement already satisfied: toml in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest==6.2.4->-r requirements.txt (line 6)) (0.10.2)
Requirement already satisfied: iniconfig in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest==6.2.4->-r requirements.txt (line 6)) (1.1.1)
Requirement already satisfied: pluggy<1.0.0a1,>=0.12 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest==6.2.4->-r requirements.txt (line 6)) (0.13.1)
Requirement already satisfied: py>=1.8.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest==6.2.4->-r requirements.txt (line 6)) (1.10.0)
Requirement already satisfied: attrs>=19.2.0 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest==6.2.4->-r requirements.txt (line 6)) (21.2.0)
Requirement already satisfied: pytest-forked in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest-xdist==2.2.1->-r requirements.txt (line 9)) (1.3.0)
Requirement already satisfied: execnet>=1.1 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest-xdist==2.2.1->-r requirements.txt (line 9)) (1.8.1)
Requirement already satisfied: apipkg>=1.4 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from execnet>=1.1->pytest-xdist==2.2.1->-r requirements.txt (line 9)) (1.5)
Requirement already satisfied: pyparsing>=2.0.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from packaging->pytest==6.2.4->-r requirements.txt (line 6)) (2.4.7)
Installing collected packages: pytest, coverage, pytest-xdist, pytest-django, pytest-cov
  Attempting uninstall: pytest
    Found existing installation: pytest 6.2.1
    Uninstalling pytest-6.2.1:
      Successfully uninstalled pytest-6.2.1
  Attempting uninstall: coverage
    Found existing installation: coverage 5.3.1
    Uninstalling coverage-5.3.1:
      Successfully uninstalled coverage-5.3.1
  Attempting uninstall: pytest-xdist
    Found existing installation: pytest-xdist 2.2.0
    Uninstalling pytest-xdist-2.2.0:
      Successfully uninstalled pytest-xdist-2.2.0
  Attempting uninstall: pytest-django
    Found existing installation: pytest-django 4.1.0
    Uninstalling pytest-django-4.1.0:
      Successfully uninstalled pytest-django-4.1.0
  Attempting uninstall: pytest-cov
    Found existing installation: pytest-cov 2.10.1
    Uninstalling pytest-cov-2.10.1:
      Successfully uninstalled pytest-cov-2.10.1
Successfully installed coverage-5.5 pytest-6.2.4 pytest-cov-2.12.1 pytest-django-4.4.0 pytest-xdist-2.2.1
```

* Run pytest - Runs ... but no tests! 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/5.tests/1.skeleton/project-regex/regex$ pytest
============================================================ test session starts =============================================================
platform linux -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
django: settings: regex.settings (from env)
rootdir: /home/karand/workspace/training.python/7.django/5.tests/1.skeleton/project-regex/regex
plugins: xdist-2.2.1, django-4.4.0, cov-2.12.1, forked-1.3.0
collected 0 items                                                                                                                            

=========================================================== no tests ran in 0.06s ============================================================
```

* Tweak `pytest.ini` and `.coveragerc`, add a silly test, and re-run
* And set enviroment variable `DJANGO_SETTINGS_MODULE` - 
    * For Windows - https://superuser.com/questions/284342/what-are-path-and-other-environment-variables-and-how-can-i-set-or-use-them
    * For Linux - `export` and `.bash_profile`
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/5.tests/1.skeleton/project-regex/regex$ pytest
============================================================ test session starts =============================================================
platform linux -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
django: settings: regex.settings (from env)
rootdir: /home/karand/workspace/training.python/7.django/5.tests/1.skeleton/project-regex/regex, configfile: pytest.ini
plugins: xdist-2.2.1, django-4.4.0, cov-2.12.1, forked-1.3.0
collected 1 item                                                                                                                             

entries/tests.py F                                                                                                                     [100%]

================================================================== FAILURES ==================================================================
_________________________________________________________ TryThisTests.test_try_this _________________________________________________________

self = <entries.tests.TryThisTests testMethod=test_try_this>

    def test_try_this(self):
>       self.assertEqual(1, 2)
E       AssertionError: 1 != 2

entries/tests.py:6: AssertionError

----------- coverage: platform linux, python 3.9.5-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
entries/__init__.py       0      0   100%
entries/admin.py         17      0   100%
entries/apps.py           4      0   100%
entries/forms.py          6      6     0%
entries/models.py        21      3    86%
entries/tests.py          4      0   100%
entries/urls.py           3      3     0%
entries/views.py         37     37     0%
-----------------------------------------
TOTAL                    92     49    47%
Coverage HTML written to dir htmlcov

========================================================== short test summary info ===========================================================
FAILED entries/tests.py::TryThisTests::test_try_this - AssertionError: 1 != 2
============================================================= 1 failed in 0.81s ==============================================================
```

### 9.2 Tests - Models and Admin UI

```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/5.tests/2.models-and-admin/project-regex/regex$ pytest
============================================================ test session starts =============================================================
platform linux -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
django: settings: regex.settings (from env)
rootdir: /home/karand/workspace/training.python/7.django/5.tests/2.models-and-admin/project-regex/regex, configfile: pytest.ini
plugins: xdist-2.2.1, django-4.4.0, cov-2.12.1, forked-1.3.0
collected 2 items                                                                                                                            

entries/tests.py ..                                                                                                                    [100%]

============================================================== warnings summary ==============================================================
entries/models.py:6
  /home/karand/workspace/training.python/7.django/5.tests/2.models-and-admin/project-regex/regex/entries/models.py:6: PytestCollectionWarning: cannot collect test class 'TestString' because it has a __init__ constructor (from: entries/tests.py)
    class TestString(models.Model):

-- Docs: https://docs.pytest.org/en/stable/warnings.html

----------- coverage: platform linux, python 3.9.5-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
entries/__init__.py       0      0   100%
entries/admin.py         17      0   100%
entries/apps.py           4      0   100%
entries/forms.py          6      0   100%
entries/models.py        21      2    90%
entries/tests.py         22      0   100%
entries/urls.py           3      0   100%
entries/views.py         37     14    62%
-----------------------------------------
TOTAL                   110     16    85%
Coverage HTML written to dir htmlcov

======================================================== 2 passed, 1 warning in 1.19s ========================================================
```

### 9.3 Tests - Views

* Add in a test, but ... there's an error - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/5.tests/3.views/project-regex/regex$ pytest
============================================================ test session starts =============================================================
platform linux -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
django: settings: regex.settings (from env)
rootdir: /home/karand/workspace/training.python/7.django/5.tests/3.views/project-regex/regex, configfile: pytest.ini
plugins: xdist-2.2.1, django-4.4.0, cov-2.12.1, forked-1.3.0
collected 3 items                                                                                                                            

entries/tests.py ..F                                                                                                                   [100%]

================================================================== FAILURES ==================================================================
____________________________________________________ HomeViewTests.test_home_view_renders ____________________________________________________

viewname = 'entries:home', urlconf = None, args = [], kwargs = {}, current_app = None

    def reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None):
        if urlconf is None:
            urlconf = get_urlconf()
        resolver = get_resolver(urlconf)
        args = args or []
        kwargs = kwargs or {}
    
        prefix = get_script_prefix()
    
        if not isinstance(viewname, str):
            view = viewname
        else:
            *path, view = viewname.split(':')
    
            if current_app:
                current_path = current_app.split(':')
                current_path.reverse()
            else:
                current_path = None
    
            resolved_path = []
            ns_pattern = ''
            ns_converters = {}
            for ns in path:
                current_ns = current_path.pop() if current_path else None
                # Lookup the name to see if it could be an app identifier.
                try:
                    app_list = resolver.app_dict[ns]
                    # Yes! Path part matches an app in the current Resolver.
                    if current_ns and current_ns in app_list:
                        # If we are reversing for a particular app, use that
                        # namespace.
                        ns = current_ns
                    elif ns not in app_list:
                        # The name isn't shared by one of the instances (i.e.,
                        # the default) so pick the first instance as the default.
                        ns = app_list[0]
                except KeyError:
                    pass
    
                if ns != current_ns:
                    current_path = None
    
                try:
>                   extra, resolver = resolver.namespace_dict[ns]
E                   KeyError: 'entries'

../../../../../.tpvenv/lib/python3.9/site-packages/django/urls/base.py:71: KeyError

During handling of the above exception, another exception occurred:

self = <entries.tests.HomeViewTests testMethod=test_home_view_renders>

    def test_home_view_renders(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )
>       response = self.client.get(reverse('entries:home',))

entries/tests.py:72: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

viewname = 'entries:home', urlconf = None, args = [], kwargs = {}, current_app = None

    def reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None):
        if urlconf is None:
            urlconf = get_urlconf()
        resolver = get_resolver(urlconf)
        args = args or []
        kwargs = kwargs or {}
    
        prefix = get_script_prefix()
    
        if not isinstance(viewname, str):
            view = viewname
        else:
            *path, view = viewname.split(':')
    
            if current_app:
                current_path = current_app.split(':')
                current_path.reverse()
            else:
                current_path = None
    
            resolved_path = []
            ns_pattern = ''
            ns_converters = {}
            for ns in path:
                current_ns = current_path.pop() if current_path else None
                # Lookup the name to see if it could be an app identifier.
                try:
                    app_list = resolver.app_dict[ns]
                    # Yes! Path part matches an app in the current Resolver.
                    if current_ns and current_ns in app_list:
                        # If we are reversing for a particular app, use that
                        # namespace.
                        ns = current_ns
                    elif ns not in app_list:
                        # The name isn't shared by one of the instances (i.e.,
                        # the default) so pick the first instance as the default.
                        ns = app_list[0]
                except KeyError:
                    pass
    
                if ns != current_ns:
                    current_path = None
    
                try:
                    extra, resolver = resolver.namespace_dict[ns]
                    resolved_path.append(ns)
                    ns_pattern = ns_pattern + extra
                    ns_converters.update(resolver.pattern.converters)
                except KeyError as key:
                    if resolved_path:
                        raise NoReverseMatch(
                            "%s is not a registered namespace inside '%s'" %
                            (key, ':'.join(resolved_path))
                        )
                    else:
>                       raise NoReverseMatch("%s is not a registered namespace" % key)
E                       django.urls.exceptions.NoReverseMatch: 'entries' is not a registered namespace

../../../../../.tpvenv/lib/python3.9/site-packages/django/urls/base.py:82: NoReverseMatch
============================================================== warnings summary ==============================================================
entries/models.py:6
  /home/karand/workspace/training.python/7.django/5.tests/3.views/project-regex/regex/entries/models.py:6: PytestCollectionWarning: cannot collect test class 'TestString' because it has a __init__ constructor (from: entries/tests.py)
    class TestString(models.Model):

-- Docs: https://docs.pytest.org/en/stable/warnings.html

----------- coverage: platform linux, python 3.9.5-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
entries/__init__.py       0      0   100%
entries/admin.py         17      0   100%
entries/apps.py           4      0   100%
entries/forms.py          6      0   100%
entries/models.py        21      2    90%
entries/tests.py         33      2    94%
entries/urls.py           3      0   100%
entries/views.py         37     14    62%
-----------------------------------------
TOTAL                   121     18    85%
Coverage HTML written to dir htmlcov

========================================================== short test summary info ===========================================================
FAILED entries/tests.py::HomeViewTests::test_home_view_renders - django.urls.exceptions.NoReverseMatch: 'entries' is not a registered names...
=================================================== 1 failed, 2 passed, 1 warning in 1.40s ===================================================
```

* Because the path isn't named! Update `urls.py` with `app_name`, and the `.html` references with `url`, and run again - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/5.tests/3.views/project-regex/regex$ pytest
============================================================ test session starts =============================================================
platform linux -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
django: settings: regex.settings (from env)
rootdir: /home/karand/workspace/training.python/7.django/5.tests/3.views/project-regex/regex, configfile: pytest.ini
plugins: xdist-2.2.1, django-4.4.0, cov-2.12.1, forked-1.3.0
collected 3 items                                                                                                                            

entries/tests.py ...                                                                                                                   [100%]

============================================================== warnings summary ==============================================================
entries/models.py:6
  /home/karand/workspace/training.python/7.django/5.tests/3.views/project-regex/regex/entries/models.py:6: PytestCollectionWarning: cannot collect test class 'TestString' because it has a __init__ constructor (from: entries/tests.py)
    class TestString(models.Model):

-- Docs: https://docs.pytest.org/en/stable/warnings.html

----------- coverage: platform linux, python 3.9.5-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
entries/__init__.py       0      0   100%
entries/admin.py         17      0   100%
entries/apps.py           4      0   100%
entries/forms.py          6      0   100%
entries/models.py        21      2    90%
entries/tests.py         33      0   100%
entries/urls.py           4      0   100%
entries/views.py         37     12    68%
-----------------------------------------
TOTAL                   122     14    89%
Coverage HTML written to dir htmlcov

======================================================== 3 passed, 1 warning in 1.27s ========================================================
```

* Details - 
    * https://docs.djangoproject.com/en/3.2/topics/testing/overview/
    * https://docs.djangoproject.com/en/3.2/topics/testing/tools/
    * https://docs.djangoproject.com/en/3.2/topics/testing/advanced/#integration-with-coverage-py
    * https://docs.djangoproject.com/en/3.2/topics/testing/tools/#assertions
    * https://docs.python.org/3/library/unittest.html#assert-methods

### 9.3 Tests - APIs

* Before running, remember to update `.coveragerc` to include `api`, and `urls.py` with `app_name` - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/7.django/5.tests/4.apis/project-regex/regex$ pytest -s
============================================================ test session starts =============================================================
platform linux -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
django: settings: regex.settings (from env)
rootdir: /home/karand/workspace/training.python/7.django/5.tests/4.apis/project-regex/regex, configfile: pytest.ini
plugins: xdist-2.2.1, django-4.4.0, cov-2.12.1, forked-1.3.0
collected 4 items                                                                                                                            

api/tests.py .
entries/tests.py ...

============================================================== warnings summary ==============================================================
entries/models.py:6
  /home/karand/workspace/training.python/7.django/5.tests/4.apis/project-regex/regex/entries/models.py:6: PytestCollectionWarning: cannot collect test class 'TestString' because it has a __init__ constructor (from: entries/tests.py)
    class TestString(models.Model):

-- Docs: https://docs.pytest.org/en/stable/warnings.html

----------- coverage: platform linux, python 3.9.5-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
api/__init__.py           0      0   100%
api/admin.py              1      1     0%
api/apps.py               4      4     0%
api/models.py             1      1     0%
api/serializers.py        9      0   100%
api/tests.py             19      0   100%
api/urls.py               7      0   100%
api/views.py              8      0   100%
entries/__init__.py       0      0   100%
entries/admin.py         17      0   100%
entries/apps.py           4      0   100%
entries/forms.py          6      0   100%
entries/models.py        21      2    90%
entries/tests.py         33      0   100%
entries/urls.py           4      0   100%
entries/views.py         37     12    68%
-----------------------------------------
TOTAL                   171     20    88%
Coverage HTML written to dir htmlcov

======================================================== 4 passed, 1 warning in 1.37s ========================================================
```

* Details - 
    * https://www.django-rest-framework.org/api-guide/testing/
    * https://www.django-rest-framework.org/api-guide/testing/#apiclient
 
 ## 10. Quickstart Django - And Angular

* First off, let's rename the `regex` project as `regex-core` - it's responsibility is for the APIs and Admin UI.

* Then, let's set up a angular project. And for that ensure Angular CLI is available - 
```
(.venv) karand@Karand-Laptop:~/workspace/training.python/8.2.django-angular$ npm install -g @angular/cli
```

* Then create a new project `regex-portal` - it's responsibility is a Portal that interacts with the APIs - 
```
(.venv) karand@Karand-Laptop:~/workspace/training.python/8.2.django-angular$ ng new regex-portal
? Would you like to add Angular routing? No
? Which stylesheet format would you like to use? CSS
CREATE regex-portal/README.md (1057 bytes)
CREATE regex-portal/.editorconfig (274 bytes)
CREATE regex-portal/.gitignore (604 bytes)
CREATE regex-portal/angular.json (3075 bytes)
CREATE regex-portal/package.json (1074 bytes)
CREATE regex-portal/tsconfig.json (783 bytes)
CREATE regex-portal/.browserslistrc (703 bytes)
CREATE regex-portal/karma.conf.js (1429 bytes)
CREATE regex-portal/tsconfig.app.json (287 bytes)
CREATE regex-portal/tsconfig.spec.json (333 bytes)
CREATE regex-portal/src/favicon.ico (948 bytes)
CREATE regex-portal/src/index.html (297 bytes)
CREATE regex-portal/src/main.ts (372 bytes)
CREATE regex-portal/src/polyfills.ts (2820 bytes)
CREATE regex-portal/src/styles.css (80 bytes)
CREATE regex-portal/src/test.ts (743 bytes)
CREATE regex-portal/src/assets/.gitkeep (0 bytes)
CREATE regex-portal/src/environments/environment.prod.ts (51 bytes)
CREATE regex-portal/src/environments/environment.ts (658 bytes)
CREATE regex-portal/src/app/app.module.ts (314 bytes)
CREATE regex-portal/src/app/app.component.css (0 bytes)
CREATE regex-portal/src/app/app.component.html (23777 bytes)
CREATE regex-portal/src/app/app.component.spec.ts (958 bytes)
CREATE regex-portal/src/app/app.component.ts (216 bytes)
```

* Run the server to confirm the defaults work, and default Angular home page loads on `http://localhost:4200/` - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/8.2.django-angular/regex-portal$ ng serve --open
⠋ Generating browser application bundles (phase: setup)...Compiling @angular/core : es2015 as esm2015
Compiling @angular/common : es2015 as esm2015
Compiling @angular/platform-browser : es2015 as esm2015
Compiling @angular/platform-browser-dynamic : es2015 as esm2015
✔ Browser application bundle generation complete.

Initial Chunk Files | Names         |      Size
vendor.js           | vendor        |   2.08 MB
polyfills.js        | polyfills     | 128.55 kB
main.js             | main          |  52.33 kB
runtime.js          | runtime       |   6.58 kB
styles.css          | styles        | 119 bytes

                    | Initial Total |   2.26 MB

Build at: 2021-06-17T05:36:19.474Z - Hash: 14f99f76bee52107c206 - Time: 18929ms

** Angular Live Development Server is listening on localhost:4200, open your browser on http://localhost:4200/ **


✔ Compiled successfully.
✔ Browser application bundle generation complete.

5 unchanged chunks

Build at: 2021-06-17T05:36:21.419Z - Hash: 3bead9f90e6c74c4b6c1 - Time: 1348ms

✔ Compiled successfully.
```

* Next, tweak so that data is pulled from the `entries` API. This involves adjusting - 
    * `app.component.html` - To loop over the data set and display
    * `app.component.ts` - To grab the entries data
    * `entry.ts` - For the model type definition
    * `entries.service.ts` - To provide a service to pull entries data from the API
    * Helper services - To handler errors `http-error-handler.service.ts` and messages `message.service.ts`
    * `app.module.ts` - To plug in core `imports` and `providers`
    * Note that all of the above is the simplest version possible. Ideally, entries would be it's own component! And routes managed appropriately. 

* Then hit http://localhost:4200/ but note that the below error crops up in the browser console since the domain on which the API is hosted disallows cross origin request by default - 
```
Access to XMLHttpRequest at 'http://localhost:8000/api/entries' from origin 'http://localhost:4200' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
```

* To whitelist domains in the API, the `django-cors-headers` is pretty convenient https://pypi.org/project/django-cors-headers/. Let's install as per usual - 
```
(.tpvenv) karand@Karand-Laptop:~/workspace/training.python/8.2.django-angular/regex-core$ pip install -r requirements.txt
Requirement already satisfied: coverage==5.5 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 1)) (5.5)
Requirement already satisfied: django==3.2.3 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 2)) (3.2.3)
Collecting django-cors-headers==3.7.0
  Using cached django_cors_headers-3.7.0-py3-none-any.whl (12 kB)
Requirement already satisfied: django-extensions==3.1.3 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 4)) (3.1.3)
Requirement already satisfied: djangorestframework==3.12.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 5)) (3.12.2)
Requirement already satisfied: pycodestyle==2.7.0 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 6)) (2.7.0)
Requirement already satisfied: pytest==6.2.4 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 7)) (6.2.4)
Requirement already satisfied: pytest-cov==2.12.1 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 8)) (2.12.1)
Requirement already satisfied: pytest-django==4.4.0 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 9)) (4.4.0)
Requirement already satisfied: pytest-xdist==2.2.1 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from -r requirements.txt (line 10)) (2.2.1)
Requirement already satisfied: pytz in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from django==3.2.3->-r requirements.txt (line 2)) (2021.1)
Requirement already satisfied: asgiref<4,>=3.3.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from django==3.2.3->-r requirements.txt (line 2)) (3.3.4)
Requirement already satisfied: sqlparse>=0.2.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from django==3.2.3->-r requirements.txt (line 2)) (0.4.1)
Requirement already satisfied: toml in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest==6.2.4->-r requirements.txt (line 7)) (0.10.2)
Requirement already satisfied: iniconfig in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest==6.2.4->-r requirements.txt (line 7)) (1.1.1)
Requirement already satisfied: packaging in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest==6.2.4->-r requirements.txt (line 7)) (20.9)
Requirement already satisfied: py>=1.8.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest==6.2.4->-r requirements.txt (line 7)) (1.10.0)
Requirement already satisfied: pluggy<1.0.0a1,>=0.12 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest==6.2.4->-r requirements.txt (line 7)) (0.13.1)
Requirement already satisfied: attrs>=19.2.0 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest==6.2.4->-r requirements.txt (line 7)) (21.2.0)
Requirement already satisfied: execnet>=1.1 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest-xdist==2.2.1->-r requirements.txt (line 10)) (1.8.1)
Requirement already satisfied: pytest-forked in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from pytest-xdist==2.2.1->-r requirements.txt (line 10)) (1.3.0)
Requirement already satisfied: apipkg>=1.4 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from execnet>=1.1->pytest-xdist==2.2.1->-r requirements.txt (line 10)) (1.5)
Requirement already satisfied: pyparsing>=2.0.2 in /home/karand/workspace/training.python/.tpvenv/lib/python3.9/site-packages (from packaging->pytest==6.2.4->-r requirements.txt (line 7)) (2.4.7)
Installing collected packages: django-cors-headers
Successfully installed django-cors-headers-3.7.0
```

* And per the docs adjust `settings.py` (add new setting, update `INSTALLED_APPS` and `MIDDLEWARE`)

* Hit http://localhost:4200/ again, and voila! The page now loads with data from the API. Note the `Preflight` request in browser console under the `Network` tab.

* Details - 
    * https://angular.io/guide/setup-local
    * https://angular.io/guide/http
    * https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
    * https://pypi.org/project/django-cors-headers/

