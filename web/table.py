from django.utils.safestring import mark_safe
import django_tables2 as tables


class Table(tables.Table):
    name = tables.Column("이름", orderable=False)
    damage = tables.Column("데미지", orderable=False)
    resource = tables.Column("자원", orderable=False)

    class Meta:
        template_name = "django_tables2/table.html"
        attrs = {"class": "table table-bordered table-hover text-center",
                 "td": {"class": "align-middle"},
                 "th": {"class": "align-middle"},
                 "style": "table-layout: fixed; word-wrap: break-word;"}
        per_page = 20
