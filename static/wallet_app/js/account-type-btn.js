// const selectBtn = document.getElementById('x-13');
// const selectDropdown = document.querySelector('.type-options-12');
// const typeInput = document.getElementById("type-input");
// let selectedOption = '';

// // Set the selected option to the first option
// const firstOption = selectDropdown.querySelector('li');
// selectedOption = firstOption.innerHTML;
// selectBtn.innerHTML = selectedOption;

// selectBtn.addEventListener('click', () => {
//   selectDropdown.classList.toggle("show");
//   selectBtn.classList.toggle("show");
// });

// document.addEventListener('click', (event) => {
//   if (!event.target.closest('.type-options-12') && event.target !== selectBtn) {
//     selectDropdown.classList.remove("show");
//     selectBtn.classList.remove("show");
//   }
// });

// selectDropdown.addEventListener('click', (event) => {
//   const button = event.target.closest('li');
//   if (button) {
//     selectedOption = button.innerHTML;
//     typeInput.value = button.value;
//     selectBtn.innerHTML = selectedOption;
//     selectDropdown.classList.remove("show");
//     selectBtn.classList.remove("show");
//   }
// });

const selectBtn = document.getElementById('x-13');
const selectDropdown = document.querySelector('.type-options-12');
const typeInput = document.getElementById("type-input");
typeInput.value = 'General'
let selectedOption = '';

// Set the selected option to the first option
const firstOption = selectDropdown.querySelector('li');
selectedOption = firstOption.textContent;
selectBtn.innerHTML = selectedOption;

selectBtn.addEventListener('click', () => {
  selectDropdown.classList.toggle("show");
  selectBtn.classList.toggle("show");
});

document.addEventListener('click', (event) => {
  if (!event.target.closest('.type-options-12') && event.target !== selectBtn) {
    selectDropdown.classList.remove("show");
    selectBtn.classList.remove("show");
  }
});

selectDropdown.addEventListener('click', (event) => {
  const button = event.target.closest('li');
  if (button) {
    selectedOption = button.textContent;
    typeInput.value = selectedOption;
    selectBtn.innerHTML = selectedOption;
    selectDropdown.classList.remove("show");
    selectBtn.classList.remove("show");
  }
});

