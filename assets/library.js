const search = document.querySelector('#search');
const clear = document.querySelector('#clear-search');
const status = document.querySelector('#search-status');
const resources = [...document.querySelectorAll('.searchable')];
function filterResources() {
  const words = search.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
  let count = 0;
  for (const resource of resources) {
    const haystack = resource.dataset.search.toLowerCase();
    resource.hidden = !words.every(word => haystack.includes(word));
    if (!resource.hidden) count++;
  }
  for (const group of document.querySelectorAll('.example-group')) {
    group.hidden = ![...group.querySelectorAll('.searchable')].some(item => !item.hidden);
  }
  for (const section of document.querySelectorAll('.collection')) {
    section.hidden = ![...section.querySelectorAll('.searchable')].some(item => !item.hidden);
  }
  clear.hidden = !search.value;
  status.hidden = !words.length;
  status.textContent = `${count} matching ${count === 1 ? 'resource or collection' : 'resources and collections'}`;
  document.querySelector('#empty-state').hidden = count > 0;
}
function resetSearch() { search.value = ''; filterResources(); search.focus(); }
search.addEventListener('input', filterResources);
clear.addEventListener('click', resetSearch);
document.querySelector('#reset-search').addEventListener('click', resetSearch);
for (const link of document.querySelectorAll('.browse-bar nav a, .index-counts a, .text-link')) {
  link.addEventListener('click', () => { if (search.value) { search.value = ''; filterResources(); } });
}
