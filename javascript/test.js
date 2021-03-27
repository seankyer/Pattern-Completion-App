function patternTest() {
    var inputText = document.getElementById("pattern").value;
    var repetition = document.getElementById("repetitions").value.toString();

    var outString = inputText.repeat(repetition);

    document.getElementById("success-alert").innerHTML = "Output:";
    document.getElementById("output").innerHTML = outString;
}




