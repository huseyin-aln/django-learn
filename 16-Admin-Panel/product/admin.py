from django.contrib import admin

# Register your models here.
from .models import Product, Review, Category
from django.utils import timezone
from django.utils.safestring import mark_safe
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from import_export.admin import ImportExportModelAdmin
from .resources import ReviewResource




class ReviewInline(admin.TabularInline):  # StackedInline different view same job
    '''Tabular Inline View for '''
    model = Review
    extra = 1
    classes = ('collapse',)
    # min_num = 3
    # max_num = 20


class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ("create_date",)
    list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago", "how_many_reviews","bring_img_to_list")
    list_editable = ( "is_in_stock", )
    list_display_links = ("create_date", ) #can't add items in list_editable to here
    search_fields = ("name", "create_date")
    prepopulated_fields = {'slug' : ('name',)}
    list_per_page = 15
    # list_filter = ("is_in_stock", "create_date", "name")
    list_filter = ("is_in_stock", ("create_date", DateTimeRangeFilter),
        ('name', DropdownFilter),
    )
    
    date_hierarchy = "update_date"
    inlines = (ReviewInline,)
    # fields = (('name', 'slug'), 'description', "is_in_stock")
    readonly_fields = ("bring_image",)
    fieldsets = (
        ("test", {
            "fields": (
                ('name', 'slug'), "is_in_stock" 
            ),
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description", "categories","product_img", "bring_image"),
            'description' : "You can use this section for optionals settings"
        })
    )
    filter_horizontal = ("categories", )
    # filter_vertical = ("categories", )
    actions = ("is_in_stock", )


    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} variety of products added to stock")
        
    is_in_stock.short_description = 'Add marked products to stock'


    def added_days_ago(self, product):
        fark = timezone.now() - product.create_date
        return fark.days

    
    def bring_img_to_list(self, obj):
        if obj.product_img:
            return mark_safe(f"<img src={obj.product_img.url} width=50 height=50></img>")
        return mark_safe("******")
    

class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    raw_id_fields = ('product',) 
    list_filter = (
        ('product', RelatedDropdownFilter),
    )
    resource_class = ReviewResource
    



admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Category)


admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway Admin Portal"  
admin.site.index_title = "Welcome to Clarusway Admin Portal"
