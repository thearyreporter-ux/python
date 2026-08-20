from khmer_quiz.questions import question1, question2, question3, question4, question5
from khmer_quiz.display import title, final_score 

def answer_question():
    score = 0
    title()

    #សំណួរទី១
    score += question1()
    print("")

    #សំណួរទី២
    score += question2()
    print("")

    #សំណួរទី៣
    score += question3()
    print("")

    #សំណួរទី៤
    score += question4()
    print("")

    #សំណួរទី៥
    score += question5()
    print("")

    final_score(score)

    while True:
        print("1. តេស្តម្តងទៀត")
        print("2. បញ្ចប់តេស្ត")
        
        restart_option = input("សូមជ្រើសរើស: ")
        match restart_option:
            case "1":
                print(f"ការតេស្តចាប់ផ្តើមម្តងទៀត!")
                print("")
                return True
            case "2":
                print("ការតេស្តត្រូវបានបញ្ចប់!")
                return False          
            case _:
                print("")
                print("ការជ្រើសរើសមិនត្រឹមត្រូវ! សូមជ្រើសរើស (1 ឬ 2) ម្តងទៀត។")   
        
