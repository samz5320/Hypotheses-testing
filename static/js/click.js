var button = document.getElementsByClassName("cybr-btn"),
  count = 0;
button.onclick = function() {
  count += 1;
  button.innerHTML = " " + count;
};
