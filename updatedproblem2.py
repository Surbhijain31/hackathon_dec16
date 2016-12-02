test_cases=int(raw_input("Enter no. of Test cases:"))

#Running a loop upto number of test cases
while(test_cases>0):
    test_cases=test_cases-1
    
    # User Input start point and destination point
    start_point=int(raw_input("Enter starting point:"))
    end_point=int(raw_input("Enter destination point:"))

    count=0      
        

    while(start_point!=end_point):
        if(start_point<end_point):
            while(start_point<end_point):
                count=count+1
                start_point=start_point*2
                print "Steps:",start_point
        if(start_point>end_point):
            start_point=start_point-1
            print "Steps:",start_point
            count =count+1
    print "Count is:",count
        
