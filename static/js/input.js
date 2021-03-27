var INPUTS = [];

function addRowCol() {
    document.getElementById("matrix").innerHTML = "";
    rows = document.getElementById("rows").value.toString();
    cols = document.getElementById("cols").value.toString();

    for(x = 0; x < rows; x++) {
        var span = document.createElement("span");
        for(y = 0; y < cols; y++) {
            var col = y.toString();
            var row = x.toString()
            var label = document.createElement("label");
            label.innerHTML = "Row: " + row + ", Col: " + col;
            var input = document.createElement("input");
            var id = y.toString() + "," + x.toString();
            input.id = id;
            span.appendChild(label);
            span.appendChild(input);
        }
        var br = document.createElement("br");
        document.getElementById("matrix").appendChild(br);
        document.getElementById("matrix").appendChild(span);
    }

    document.getElementById("dimensions-tag").innerHTML = rows + ", " + cols
}
