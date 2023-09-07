class Person:
    name = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'There is no such user'
        else:
            return self.name[user_id]
        
    def TowerOfHanoi(n , source, destination, auxiliary):
        if n==1:
            print ("Move disk 1 from source",source,"to destination",destination)
            return
        TowerOfHanoi(n-1, source, auxiliary, destination)
        print ("Move disk",n,"from source",source,"to destination",destination)
        TowerOfHanoi(n-1, auxiliary, destination, source)


    def fibonacci_of(n):
        if n in {0, 1}:  # Base case
            return n
        return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case

if __name__ == '__main__':
    person = Person()
    print('User Abbas has been added with id ', person.set_name('Abbas'))
    print('User associated with id 0 is ', person.get_name(0))