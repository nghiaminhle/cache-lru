from cache_item import CacheItem

class LRUCache:
    maps = {}
    size = 0
    first = None
    last = None

    def __init__(self, size):
        self.size = size

    def add(self, key, value):
        if self.first == None:
            item = CacheItem(key, value)
            self.first = item
            self.last = item
            self.maps[key] = item
            return
        
        if key in self.maps:
            item = self.maps[key]            
            self.__change_cache_order(item)
            item.value = value
        else:
            if (len(self.maps)==self.size):
                self.remove(self.first.key)
            item = CacheItem(key, value)
            item.previous_item = self.last
            self.last.next_item = item
            self.last = item
            self.maps[key] = item
    
    def get(self, key):
        if key in self.maps.keys():
            item = self.maps[key]
            self.__change_cache_order(item)
            return item.value
        return None

    def remove(self, key):
        if key in self.maps.keys():
            item = self.maps[key]
            self.__change_cache_order(item)
            if item.previous_item !=None:
                self.last = item.previous_item
                item.previous_item.next_item = None
                item.previous_item = None
            else:
                self.first = None
                self.last = None
            del self.maps[key]
    
    def __change_cache_order(self, item):
        if item.next_item == None:
            return
        item.next_item.previous_item = item.previous_item
        if item.previous_item != None:
            item.previous_item.next_item = item.next_item            
        else:
            self.first = item.next_item
        self.last.next_item = item
        item.previous_item = self.last
        item.next_item = None
        self.last = item

    def get_cache_space(self):
        return len(self.maps)

def main():
    cache_store = LRUCache(5)
    
    cache_store.add('1', 1)
    assert cache_store.get('1') == 1
    assert cache_store.first.key == '1'
    assert cache_store.last.key == '1'
    
    cache_store.add('2', 2)
    assert cache_store.get('2') == 2
    assert cache_store.first.key == '1'
    assert cache_store.last.key == '2'
    
    cache_store.add('3', 3)
    assert cache_store.get('3') == 3
    assert cache_store.first.key == '1'
    assert cache_store.last.key == '3'
    
    cache_store.add('4', 4)
    assert cache_store.get('4') == 4
    assert cache_store.first.key == '1'
    assert cache_store.last.key == '4'
    
    cache_store.add('5', 5)
    assert cache_store.get('5') == 5
    assert cache_store.first.key == '1'
    assert cache_store.last.key == '5'

    cache_store.add('5', 6)
    assert cache_store.get('5') == 6
    assert cache_store.first.key == '1'
    assert cache_store.last.key == '5'
    
    cache_store.add('6', 6)
    assert cache_store.get('6') == 6
    assert cache_store.get_cache_space() == 5
    assert cache_store.get('1') == None
    assert cache_store.first.key == '2'
    assert cache_store.last.key == '6'

    cache_store.remove('2')
    assert cache_store.get('2') == None
    assert cache_store.get_cache_space() == 4
    assert cache_store.first.key == '3'
    assert cache_store.first.previous_item == None
    assert cache_store.last.key == '6'
    
    cache_store.add('3', 4)
    assert cache_store.get('3') == 4
    assert cache_store.first.key == '4'
    assert cache_store.first.previous_item == None
    assert cache_store.last.key == '3'
    
    cache_store.add('4', 6)
    assert cache_store.get('4') == 6
    assert cache_store.first.key == '5'
    assert cache_store.last.key == '4'

    cache_store.add('4', 1)
    assert cache_store.get('4') == 1
    assert cache_store.last.key == '4'

    cache_store.add('7', 7)
    assert cache_store.get('7') == 7
    assert cache_store.get_cache_space() == 5
    assert cache_store.last.key == '7'

    cache_store.add('8', 8)
    assert cache_store.get('8') == 8
    assert cache_store.last.key == '8'

    assert cache_store.get('5') == None
    cache_store.remove('3')
    assert cache_store.get('3') == None
    cache_store.remove('4')
    assert cache_store.get('4') == None
    cache_store.remove('6')
    assert cache_store.get('6') == None
    cache_store.remove('7')
    assert cache_store.get('7') == None
    cache_store.remove('8')
    assert cache_store.get('8') == None
    
    assert cache_store.get_cache_space() == 0


if __name__ == "__main__":
    main()