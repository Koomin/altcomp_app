from simple_history.admin import SimpleHistoryAdmin


class HistoryAdmin(SimpleHistoryAdmin):
    readonly_fields = ['created', 'modified']
