from pyscript import document, display

members = ["JunJun Otot", "Kim Burghly", "Kristin Ligaya", "Yvonne Adarna", "Alfred Kaso", "Khaleb Burba", "Kurt Cochinillo", "Mary Tinola", "Jill Whamos", "Anna Onse"]

def check_name(event=None):
    first = document.getElementById("first-name").value
    last = document.getElementById("last-name").value

    name = first.strip() + " " + last.strip()

    result = document.getElementById("result")

    if name in members:
        result.innerHTML = "Welcome, " + name + "! You are an ICT Club member."
        result.className = "result success"
    else:
        result.innerHTML = "Sorry, " + name + ". Your name is not on the list."
        result.className = "result error"
