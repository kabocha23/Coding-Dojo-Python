class Call(object): # storing details of all calls coming in
    
    def __init__(self,unique_id,caller_name,caller_phone,time,reason):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.time = time
        self.reason = reason

    def Display(self):
        print self.unique_id
        print self.caller_name
        print self.caller_phone
        print self.time
        print self.reason
        
caller1 = Call(000001,"Jason Kobuchi","415 555 5555","17:45","Broken thumb")
caller2 = Call(000002,"Reginald Wallace","650 555 5555","17:57","Broken pinky")
caller3 = Call(000003,"Sean Connery","707 555 5555","18:13","Broken ring finger")
caller4 = Call(000004,"Frank Sinatra","808 555 5555","18:21","Broken index finger")
caller5 = Call(000005,"Ricky Bobby","808 555 5555","18:35","Broken pinky toe")

# caller1.Display()
# caller2.Display()
# caller3.Display()
# caller4.Display()


class CallCenter(object): # storing calls coming in

    def __init__(self):
        self.calls = [] # list of all call objects
        self.queue_size = 0 # length of the call list

    def Add(self,caller):
        self.calls.append(caller)
        self.queue_size += 1
        return self

    def Remove(self):   
        self.calls.pop(0)
        self.queue_size -= 1
        return self

    def Info(self):
        for element in self.calls:
            print element.caller_name, element.caller_phone
        # print self.calls[1].caller_name
        print self.queue_size
        return self

test_calls = CallCenter()

test_calls.Add(caller1).Add(caller2).Add(caller3).Add(caller4).Add(caller5).Remove().Info()