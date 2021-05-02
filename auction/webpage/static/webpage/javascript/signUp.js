$("#signUpForm").submit(function () {
    const email = document.querySelector("#email").value
    const password1 = document.querySelector("#password1").value
    const password2 = document.querySelector("#password2").value

    if (password1 == password2 && email.includes("@")) {
        return true
    }

    tempNotify("Passordene stemte ikke, eller email var feil", "error")
    return false
})
