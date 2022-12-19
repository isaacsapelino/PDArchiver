const switchToStudent = document.querySelector("#switchToStudent");
const switchToFaculty = document.querySelector("#switchToFaculty");
const facultyLoginContainer = document.querySelector("#facultyLoginContainer");
const studentLoginContainer = document.querySelector("#studentLoginContainer");
const loginScreenBoxBottom = document.querySelector("#loginScreenBottomText");


let getButtons = (e) => e.preventDefault();

switchToStudent.addEventListener("click", (e) => {

    if (studentLoginContainer.classList.contains("isHidden")) {
        studentLoginContainer.classList.remove("isHidden");
        studentLoginContainer.classList.add("show");
        loginScreenBoxBottom.classList.remove("isHidden");
        loginScreenBoxBottom.classList.remove("isHidden");
    } else {
        studentLoginContainer.classList.add("show");
    }

    if (switchToFaculty.classList.contains("isSelected")) {
        switchToFaculty.classList.remove("isSelected");
        facultyLoginContainer.classList.add("isHidden");
        facultyLoginContainer.classList.remove("show");
        switchToStudent.classList.add("isSelected");
    } else {
        switchToStudent.classList.add("isSelected");
    }
    
});

switchToFaculty.addEventListener("click", (e) => {

    if (facultyLoginContainer.classList.contains("isHidden")) {
        facultyLoginContainer.classList.remove("isHidden");
        facultyLoginContainer.classList.add("show");
        loginScreenBoxBottom.classList.add("isHidden");
    } else {
        facultyLoginContainer.classList.add("show");
        loginScreenBoxBottom.classList.add("isHidden");
    }

    if (switchToStudent.classList.contains("isSelected")) {
        switchToStudent.classList.remove("isSelected");
        studentLoginContainer.classList.add("isHidden");
        studentLoginContainer.classList.remove("show");
        switchToFaculty.classList.add("isSelected");
    } else {
        switchToFaculty.classList.add("isSelected");
    }
});