import django_tables2 as tables


class StatusTable(tables.Table):
    name = tables.Column("이름", orderable=False)
    damage = tables.Column("데미지", orderable=False)
    resource = tables.Column("자원", orderable=False)

    class Meta:
        template_name = "django_tables2/table.html"
        attrs = {"class": "table table-bordered table-hover text-center",
                 "td": {"class": "align-middle"},
                 "th": {"class": "align-middle"}}


class UpgradeChartTable(tables.Table):
    current = tables.Column("현재단계", orderable=False)
    next = tables.Column("다음단계", orderable=False)
    resource = tables.Column("필요자원", orderable=False)

    class Meta:
        template_name = "django_tables2/table.html"
        attrs = {"class": "table table-bordered table-hover text-center",
                 "td": {"class": "align-middle"},
                 "th": {"class": "align-middle"}}
