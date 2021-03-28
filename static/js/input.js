// DEPRECATED

var INPUTS = [];

function addRowCol() {
    document.getElementById("matrix").innerHTML = "";
    rows = document.getElementById("rows").value.toString();
    cols = document.getElementById("cols").value.toString();

    for(let y = 0; y < rows; y++) {
        var span = document.createElement("span");
        for(let x = 0; x < cols; x++) {
            var usercol = (x+1).toString();
            var userrow = (y+1).toString()
            var label = document.createElement("label");
            label.innerHTML = "Row " + userrow + ", Col " + usercol + ":";
            var input = document.createElement("input");
            var location = x.toString() + "," + y.toString();
            input.id = location;
            span.appendChild(label);
            span.appendChild(input);
        }
        var br = document.createElement("br");
        document.getElementById("matrix").appendChild(br);
        document.getElementById("matrix").appendChild(span);
    }
    // document.getElementById("dimensions-tag").innerHTML = rows + "x" + cols
    document.getElementById("cols-terrible-storage").innerHTML = cols;
    document.getElementById("rows-terrible-storage").innerHTML = rows;
}
