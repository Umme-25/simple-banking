balance = 0.0
kyc_documents = {}
def check_balance():
    print("Your current balance is :",{balance})
    print("=======================")

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
    else:
        print("Can not deposite a negative or zero value")
        print("=======================")
    
def withdraw(amount):
    global balance
    if amount <= 0:
        print("Can not withdraw a negative or zero amount")
    elif amount > balance:
        print("Can not withdraw. Insufficient balance.")
    else:
        balance -= amount
        print("=======================")

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("Kyc not done")
        print("=======================")
    else:
        for doc in kyc_documents:
          print(f"{doc}: {kyc_documents[doc]}")

        print("=======================")


if __name__ == "__main__":
    print("=======================")
    print("Welcome to ABC bank!!!")
    print("=======================")

    while True:
        print("1.check your balance")
        print("2. Deposite an amount")
        print("3. Withdraw an amount")
        print("4. Check kyc")
        print("5. Update kyc")
        print("6. Quit")
        choice =input("Enter your choice (1-6):")
        print("=======================")
        if choice == '1':
            check_balance()
        elif choice == '2':
            amt = float(input("Enter the amount to deposite:"))
            deposit(amt)
            print(f"Amount {amt} deposited successfully")
            print("=======================")
        elif choice == '3':
            amt = float(input("Enter the amount to withdrw:"))
            withdraw(amt)
            print(f"Amount {amt} withdrawn successfully")
            print("=======================")
        elif choice == '4':
            check_kyc()
        elif choice == '5':
            kyc_docs = {}
            n_documents = int(input("Enter the number of documents you want to add:"))
            for i in range(n_documents):
                key = input("Enter the document type: ")
                value = input("Enter the document number:")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print(f"KYC updated!")
            print("=======================")
        elif choice == '6':
            print("Quiting, have a nice day.")
            break  #prevents from infinite loop
        else:
            print("Invalid choice!!! Re-try.")
            print("=======================")

    print()
    print("Thankyou for banking with us:)")