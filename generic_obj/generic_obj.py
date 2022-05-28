from uuid import uuid4


class GenericObj:
    def __init__(self, **kwargs):
        self._uuid = str(uuid4())
        self.__dict__.update(kwargs)
        
    def get(self, obj = None):
        if obj is None:
            return self.__get_all()
        elif isinstance(getattr(self,obj), self.__class__):
            return self.__get_self_obj(obj)
        elif isinstance(getattr(self,obj), list):
            return self.__get_list_vals(obj)
        elif isinstance(getattr(self, obj), dict):
            return self.__get_dict_vals(obj)
        return getattr(self,obj)
    
    def __get_dict_vals(self, obj):
        dict_obj = getattr(self,obj)
        values = {}
        for k in dict_obj:
            if isinstance(dict_obj[k], self.__class__):
                values[k] = dict_obj[k].get()
            else:
                values[k] = dict_obj[k]
        return values
    
    def __get_self_obj(self, obj):
        values = {}
        instance_dict = getattr(self,obj).__dict__
        for k in instance_dict:
            values[k] = getattr(self,obj).get(k)
        return values
    
    def __get_list_vals(self, obj):
        if isinstance(getattr(self,obj)[0], self.__class__):
            list_vals = getattr(self, obj)
            list_objs = []
            for k in list_vals:
                instance_dict = k.__dict__
                values = {}
                for j in instance_dict:
                    values[j] = k.get(j)
                list_objs.append(values)
            return list_objs
        else:
            return getattr(self,obj)

    def __get_all(self):
        values = {}
        for k in self.__dict__:
            values[k] = self.get(k)
        return values