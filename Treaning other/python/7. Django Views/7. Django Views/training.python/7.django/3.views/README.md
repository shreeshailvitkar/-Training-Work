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
System check identified some issues:

WARNINGS:
entries.Entry: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the EntriesConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
Migrations for 'entries':
  entries/migrations/0001_initial.py
    - Create model Entry
```
* Note the warning around `BigAutoField` which is newly available in Django 3.2, and is recommended to be used as primary key. So -
    * Update `settings.py` to use the right `DEFAULT_AUTO_FIELD`
    * Delete the newly created migration file under `entries/migrations/0001_initial.py`, and rerun `makemigrations`
    * And note the warning no longer shows up
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
