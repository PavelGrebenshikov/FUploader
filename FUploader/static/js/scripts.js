window.onload = () => {
    let bubble = document.querySelector(".wps-block");
    const btnUpload = document.querySelector(".btn-upload");
    const fileUpload = document.getElementById("fileUpload");
    const fileName = document.querySelector(".file-text");

    bubble.addEventListener("mouseover", () => {
        bubble.classList.toggle("border-bubble");
    });

    bubble.addEventListener("mouseout", () => {
        bubble.classList.remove("border-bubble");
    });

    btnUpload.addEventListener("click", () => {
        fileUpload.click();
    });

    fileUpload.addEventListener("change", () => {
        fileExtension = fileUpload.files[0].name.split('.').pop();
        if (fileExtension === 'txt') {
            if (fileUpload.value) {
                fileName.innerHTML = fileUpload.value.match(/[\/\\]([\w\d\s\.\-(\)]+)$/)[1];
            } else {
                fileName.innerHTML = "No file selected";
            };
            const btnToSend = document.querySelector(".to-send");
            btnToSend.click();
        } else {
            fileName.innerHTML = "The file does not match the extension .txt";
        };
    });
}