from django.contrib.admin import AdminSite as DjangoAdminSite

class AdminSite(DjangoAdminSite):
    site_header = 'Tanabeles Login'
    site_title = 'Tanabeles Admin'

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been registered in this site.
        """
        app_dict = self._build_app_dict(request)
        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])

        # Move the 'store' app to the top.
        store_app = next((app for app in app_list if app['app_label'] == 'store'), None)
        if store_app:
            app_list.remove(store_app)
            app_list.insert(0, store_app)

        return app_list

admin_site = AdminSite(name='myadmin')