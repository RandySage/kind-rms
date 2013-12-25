from django.contrib import admin

from sqleditoronline.models import SqlTable, TableRow

admin.site.register(TableRow)
admin.site.register(SqlTable)
