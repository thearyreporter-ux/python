def answer_question():
    global score
    score = 0

    print("-" * 30)
    print("      KHMER TOURISM QUIZ")
    print("-" * 30)
    print("")

    #សំណួរទី១
    print("សំណួរទី​១ :")
    print("* តើសិល្បៈខ្មែរចែកជាប៉ុន្មានរចនាបថ? ")
    print ("ក. ១០")
    print ("ខ. ១៣ ")
    print ("គ. ១៤ ")
    option_1 = input("សូមជ្រើសរើសចម្លើយ (ក - គ): ")
    match option_1:
        case "គ":
            print(f"ចម្លើយ : {option_1} គឹត្រឹមត្រូវ = 20 ពិន្ទុ")
            score += 20
        case _:
            print("ចម្លើយមិនត្រូវត្រូវ = 0 ពិន្ទុ")

    print("")

    #សំណួរទី​២
    print("សំណួរទី​ ២ :")
    print("* តើប្រទេសកម្ពុជាប្រកាន់យកសាសនាអ្វីជាផ្លូវការនាបច្ចុប្បន្ននេះ? ")
    print ("ក. ពុទ្ធសាសនា")
    print ("ខ. សាសនាឥស្លាម ")
    print ("គ. សាសនាព្រាហ្មណ៍ ")      
    option_2 = input("សូមជ្រើសរើសចម្លើយ (ក-គ): ")        
    match option_2:
        case "ក":
            print(f"ចម្លើយ : {option_2} គឹត្រឹមត្រូវ = 20 ពិន្ទុ")
            score += 20
        case _:
            print("ចម្លើយមិនត្រូវត្រូវ = 0 ពិន្ទុ")

    print("")

    #សំណួរទី៣
    print("សំណួរទី​ ៣​ :")
    print("* តើកម្ពុជាទទួលបានឯករាជ្យពីអាណាព្យាបាលបារាំងនៅឆ្នាំណា?")
    print ( " ក. ឆ្នាំ ១៩៤៥ " )
    print ( " ខ. ឆ្នាំ ១៩៥៣ " )
    print ( " គ. ឆ្នាំ​ ១៩៦៣ " )
    option_3 = input("សូមជ្រើសរើសចម្លើយ (ក-គ): ")        
    match option_3:
        case "ខ":
            print(f"ចម្លើយ : {option_3} គឹត្រឹមត្រូវ = 20 ពិន្ទុ")
            score += 20
        case _:
            print("ចម្លើយមិនត្រូវត្រូវ = 0 ពិន្ទុ")

    print ("")

    #សំណួរទី៤
    print("សំណួរទី​ ៤​ :")
    print("* តើប្រព័ន្ធគមនាគមន៍ផ្លូវទឹកនៅអង្គរមានប៉ុន្មាន?")
    print ( " ក. ១ " )
    print ( " ខ. ២ " )
    print ( " គ. ៣ " )
    option_4 = input("សូមជ្រើសរើសចម្លើយ (ក-គ): ")        
    match option_4:
        case "ខ":
            print(f"ចម្លើយ : {option_4} គឹត្រឹមត្រូវ = 20 ពិន្ទុ")
            score += 20
        case _:
            print("ចម្លើយមិនត្រូវត្រូវ = 0 ពិន្ទុ")

    print ("")

    #សំណួរទី៥
    print("សំណួរទី​ ៥​ :")
    print("* តើមរតកវប្បធម៌ ឬបេតិកភណ្ខវប្បធម៌ចែកចេញជាប៉ុន្មាន? អ្វីខ្លះ?")

    print ( " ក. ចែកចេញជា ២ គឺ បេតិកភណ្ខវប្បធម៌ធម្មជាតិ និងបេតិកភណ្ខវប្បធម៌រូបី " )
    print ( " ខ. ចែកចេញជា ៣ គឺ បេតិកភណ្ខវប្បធម៌ធម្មជាតិ បេតិកភណ្ខវប្បធម៌រូបី និងបេតិកភណ្ខវប្បធម៌អរូបី " )
    print ( " គ. ចែកចេញជា ២ គឺ បេតិកភណ្ខវប្បធម៌រូបី និងបេតិកភណ្ខវប្បធម៌អរូបី " )
    option_5 = input("សូមជ្រើសរើសចម្លើយ (ក-គ): ")        
    match option_5:
        case "គ":
            print(f"ចម្លើយ : {option_5} គឹត្រឹមត្រូវ = 20 ពិន្ទុ")
            score += 20
        case _:
            print("ចម្លើយមិនត្រូវត្រូវ = 0 ពិន្ទុ")

    print("")
    print("-" * 30)
    print(f"     ពិន្ទុសរុប = {score}/100")
    print("-" * 30)

    print("")

    while True:
        print("1. តេស្តម្តងទៀត")
        print("2. បញ្ចប់តេស្ត")

        restart_option = input("សូមជ្រើសរើស: ")
        match restart_option:
            case "1":
                print(f"តេស្តចាប់ផ្តើមម្តងទៀត")
                return True
            case "2":
                print("ការតេស្តត្រូវបានបញ្ចប់!")
                return False
                
            case _:
                print("")
                print("ការជ្រើសរើសមិនត្រឹមត្រូវ! សូមជ្រើសរើស (1 ឬ 2) ម្តងទៀត។")


while True:
    restart_option = answer_question() 
    if restart_option == False :
        break
    
