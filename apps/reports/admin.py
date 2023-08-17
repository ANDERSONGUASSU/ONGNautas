from django.contrib import admin
from .models import Report, Sheet


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Denúncia', {'fields': ('title', 'description',)}),
        ('Informações de Endereço', {'fields': ('cep', 'address', 'complement')}),
        ('Mídia', {'fields': ('evidence_image',)})
    )

    list_display = ('title',)
    search_fields = ('title', 'cep', 'address')
    ordering = ('title',)

    readonly_fields = ['title', 'description', 'cep', 'address', 'complement', 'evidence_image']


admin.site.register(Sheet)
