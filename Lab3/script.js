function newElement() {
    let li = document.createElement("li");
    let inputValue = document.getElementById("input").value;
    let t = document.createTextNode(inputValue);
    li.appendChild(t);
    if (inputValue === '') {
      alert("Task is empty!");
    } else {
      document.getElementById("list").appendChild(li);
    }
    document.getElementById("input").value = "";
  
    let span = document.createElement("SPAN");
    let txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    li.appendChild(span);
    delAction();
  }

  function delBtn() {
    let nodelist = document.getElementsByTagName("LI");
    let i;
    for (i = 0; i < nodelist.length; i++) {
        let span = document.createElement("SPAN");
        let txt = document.createTextNode("\u00D7");
  
        span.className = "close";
        span.appendChild(txt);
        nodelist[i].appendChild(span);
    }
  }


  
  function delAction(){
    let close = document.getElementsByClassName("close");
    let k;
    for (k = 0; k < close.length; k++) {
      close[k].onclick = function() {
        let note = this.parentElement;
        note.style.display = "none";
      }
    }
  }


  function checkClick() {
    let list = document.querySelector('ul');
    list.addEventListener('click', function(v) {
      if (v.target.tagName === 'LI') {
        v.target.classList.toggle('checked');
      }
    }, false);

  }

  delBtn();
  delAction();
  checkClick();