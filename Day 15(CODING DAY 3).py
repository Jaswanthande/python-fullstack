"""
        REMOVE SAME NUMBERS IN LIST WITHOUT BUILD IN FUNCTION

            num = [22, 4, 22, 4, 6, 7]
            empty_ = []
            def remove(num, empty_):
                for j in num:
                    if j not in empty_:
                        empty_.append(j)
                print(empty_)

            remove(numbers, empty_)


        WITH USING BUILD IN FUNCTION
            my_list = [1, 2, 2, 3, 4, 4, 5]
            unique_list = list(set(my_list))
            print(unique_list)


        FINDING A PRIME NUMBER WITHOUT USING BUILD IN FUNCTION
            prime = 7
            count =0
            def prime_not(prime,count):
                for i in range(1,prime+1):
                    if prime % i == 0:
                        count += 1
                if count == 2 :
                    
                    print("PRIME")
                else:
                    print("NOT A PRIME")
                    
            prime_not(prime,count)


        FINDING HOW MANY WHERE  PRESENTED IN INPUT WITHOUT USING BUILD IN FUNCTION
            some = "PYTHON IS A programming language"
            count =0
            def counting(some,count):
                so = some.split(' ')
                for i in so:
                    count += 1
                print(count)
            counting(some,count)


        FINDING HOW MANY CAPTIAL,SMALL AND SPACES WHERE PRESENTED IN A STRING
            some = "PYTHON IS A programming language"
            cap_count = 0
            small_count = 0
            space_count = 0
            def so(some,cap_count,small_count,space_count):
                for i in some:
                    if i.isupper():
                        cap_count += 1
                    elif i.islower():
                        small_count += 1
                    else:
                        space_count += 1
                print(f"THERE TOATAL {cap_count} NUMBER CAP")
                print(f"THERE TOATAL {small_count} NUMBER SAMLL")
                print(f"THERE TOATAL {space_count} NUMBER space count")
            so(some,cap_count,small_count,space_count)

"""


    


















