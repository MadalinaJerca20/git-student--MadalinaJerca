var table = document.getElementById("priceTable");

var i = 1;
var sum = 0;
while (i < table.rows.length) {
    sum += parseFloat(table.rows[i].cells[2].innerHTML)
    i++;
}

var row = table.insertRow(i);
var cell1 = row.insertCell(0);
var cell2 = row.insertCell(1);
var cell3 = row.insertCell(2);

cell2.innerHTML = "Total Price";
cell3.innerHTML = sum;