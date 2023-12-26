from django.db.models import Model
from asgiref.sync import sync_to_async
from app.apps.core.DTO import DTO


class BaseRepository:
    model:Model
    
    def to_list(sql):
        return [item for item in sql]
    
    
    @sync_to_async
    def delete_all(self):
        return self.model.objects.all().delete()
    
    @sync_to_async
    def get_all(self,  **args):
        query = self.model.objects

        if (args):
            query = query.filter(**args)

        return self.to_list(query.all())
    
    @sync_to_async
    def exists(self, **args):
        if not args:
            raise Exception('No have params')
        
        return self.model.objects.filter(**args).exists()
    
    
    @sync_to_async
    def update(self, search_args, update_args: any, return_model=False):
        result = self.model.objects.filter(**search_args).update(**update_args)
        
        if (result ):
            if return_model:
                
                return self.model.objects.filter(telegram_id=id).first()
            else:
                return result
        
        return False
       

    @sync_to_async
    def find_and_update(self, **args):
         return self.update(**args, return_model=True)
     
     
    @sync_to_async
    def  create(self, data:any):
        if  isinstance(data, DTO):
            return self.model.objects.create(**data.to_dict())
        
        if  isinstance(data, dict):
            return self.model.objects.create(**data)
        
        if  isinstance(data, list):
            return self.model.objects.create(data)
    
        return self.model.objects.create(data)
    
        