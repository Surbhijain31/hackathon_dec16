test_cases=int(raw_input("Enter no. of Test cases:"))

#Running a loop upto number of test cases
while(test_cases>0):
    test_cases=test_cases-1
    
    # User Input start point and destination point
    start_point=int(raw_input("Enter starting point:"))
    end_point=int(raw_input("Enter destination point:"))

    #Giving flag values to check even or odd start and destination points
    #Assigned even as 0 and odd as 1
    flag_start=0
    flag_end=0
    if(start_point%2==0):
        flag_start=0
    else:
        flag_start=1
    if(end_point%2==0):
        flag_end=0;
    else:
        flag_end=1;

    #Checking if we have to move forward or backward
        #In forward direction
    if(start_point<end_point):
        count=0

        #Moving in mutlples of 2
        if(flag_start==flag_end):
            print "Move in multiples of 2 steps"
            while(start_point!=end_point):
                count=count+1
                start_point=start_point+2
                print "Steps:",start_point
            print "Count is:",count

        #Moving in multiples of 2 and 1 step backwards
        else:
            print "Move in multiples of 2 steps and 1 step backwards"
            while(start_point!=end_point):
                count=count+1
                start_point=start_point+2
                print "Steps:",start_point
                if(start_point>end_point):
                    start_point=start_point-1
                    count=count+1
                    print "Steps:",start_point
            print "Count is:",count
                    
    #In backward direction
    #Moving 1-1 steps backward
    else:
        print "Move Backwards........."
        count=0
        while(start_point!=end_point):
            start_point=start_point-1;
            count=count+1
            print "Steps:",start_point
        print "Count is:",count
          
