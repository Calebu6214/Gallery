$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })
  
const copyBtns = [...document.getElementsByClassName('copy-btn')]
console.log(copyBtns)
copyBtns.forEach(btn=> btn.addEventListener('click', ()=>{
  console.log('click')
  const url = btn.getAttribute('data-hex')
  console.log(url)
  navigator.clipboard.writeText(url)
  btn.textContent = 'Copied'
} ))