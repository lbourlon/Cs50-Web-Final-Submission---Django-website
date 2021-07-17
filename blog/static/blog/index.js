current_page = 1;
current_category = "all";
search_type = false;

document.addEventListener('DOMContentLoaded', function() {

    //objects that apear in the body
    article_list = document.getElementById('article_list');
    single_article = document.getElementById('single_article');
    
    // Pagination objects
    prev_page = document.getElementById("previous-page");
    home_page = document.getElementById("home-page");
    next_page = document.getElementById("next-page");

    pagination_event_listeners();
    //SearchBar objects
    search_input = document.getElementById('search-input');
    search_button = document.getElementById('search-button');
    search_input.value = "";

    art_week = document.getElementById('art_id');
    music_week = document.getElementById('music_id');

    prev1 = document.getElementById('prev1')
    prev2 = document.getElementById('prev2')

    prev1.addEventListener('click', ()=> {
        load_and_display_one_article(art_week.innerText);
    })

    prev2.addEventListener('click', ()=> {
        load_and_display_one_article(music_week.innerText);
    })



    search_button.addEventListener('click', (event) => {
        event.preventDefault();
        if(search_input.value === ''){
            alert("Make sure to enter something in the search bar.");
        } else {
            document.getElementById("search_message_master").style.display = "block";
            document.getElementById("search_string").innerText = search_input.value;

            search_type = true;
            load_articles(current_category, 1)
 
        }
   });


    //load articles all categories by default
    load_articles(current_category, current_page);

    add_event_listeners_to_categories();
    add_event_listeners_to_prevs();

    subscribe_element = document.getElementById("subscribe");
    subscribe_element.addEventListener('click', () => subscribe());

})

function add_event_listeners_to_prevs(){
    const prev1 = document.getElementById("prev1");
    const prev2 = document.getElementById("prev2");

    prev1.addEventListener('mouseover', () => {
        prev1.classList.add("border-dark");
        prev1.classList.remove("border-light");
        prev1.style.backgroundColor = "lightgrey";
    });

    prev1.addEventListener('mouseout', () => {
        prev1.classList.remove("border-dark");
        prev1.classList.add('border-light')
        prev1.style.backgroundColor = "inherit";
    });

    prev2.addEventListener('mouseover', () => {
        prev2.classList.add("border-dark");
        prev2.classList.remove("border-light");
        prev2.style.backgroundColor = "lightgrey";
    });

    prev2.addEventListener('mouseout', () => {
        prev2.classList.remove("border-dark");
        prev2.classList.add('border-light')
        prev2.style.backgroundColor = "inherit";
    })

}


//Adds the event listeners to the pagination buttons
function pagination_event_listeners(){
    prev_page.addEventListener('click', () => load_articles(current_category, current_page - 1));
    home_page.addEventListener('click', () => load_articles("all", 1));
    next_page.addEventListener('click', () => load_articles(current_category, current_page + 1));
}


//give the dropdown selectors their event Listeners
function add_event_listeners_to_categories(){
    category_selectors = document.getElementsByClassName("category-selector");
    Array.from(category_selectors).forEach( selector => {
       selector.addEventListener("click", () => load_articles(selector.id.toLowerCase(), current_page));
    });
}

//function to display and hide different nav buttons for the pagination
function update_pagination(number_of_pages) {
    if(number_of_pages === 1){
        prev_page.style.display = "none";
        home_page.style.display = "none";
        next_page.style.display = "none";
    } else if (current_page === 1){
        prev_page.style.display = "none";
        home_page.style.display = "none";
        next_page.style.display = "block";
    } else if (current_page === number_of_pages){
        prev_page.style.display = "block";
        home_page.style.display = "block";
        next_page.style.display = "none";
    } else {
        prev_page.style.display = "block";
        home_page.style.display = "block";
        next_page.style.display = "block";
    }    
}

//function to display or hide the paginator object
function hide_paginator(bool){
    const paginator = document.getElementById('paginator');
    if(bool === true) paginator.style.display = "none";
    else paginator.style.display = "block";
}

//function to update the current page and category
function update_vars(category, page){
    current_page = page;
    if(current_category !== category){
        clear_articles_from_page();
        current_page = 1;
        current_category = category;
    }
}


//displays a list of articles in the main body of the page
function display_articles(articles){
    article_list.style.display = "block";
    single_article.style.display = "none";

    articles.forEach(article => {
        //declaring each component
        const article_preview_div = document.createElement('div'); 
        article_preview_div.style.cursor = "pointer";

        const title = document.createElement('h3');
        const preview_text = document.createElement('div');
        const author = document.createElement('span');
        const pub_date = document.createElement('p');

        //classes on each component
        title.classList.add('preview-title')
        article_preview_div.classList.add("article-preview", "border","rounded" ,"border-light");
        preview_text.classList.add("article-preview-body");
        author.classList.add('ml-auto');
        pub_date.classList.add('ml-auto');

        //ids
        article_preview_div.id = article.id;

        //InnerText
        title.innerText = article.title; 
        preview_text.innerText = article.preview_text;
        author.innerText = "by " + article.author;
        pub_date.innerText = "On " +  article.pub_date;

        //to load one specific article
        article_preview_div.addEventListener('click', () => load_and_display_one_article(article.id));

        article_list = document.getElementById('articles');

        article_preview_div.addEventListener('mouseover', () => {
            article_preview_div.classList.add("border-dark");
            article_preview_div.classList.remove("border-light");
            article_preview_div.style.backgroundColor = "lightgrey";
        });

        article_preview_div.addEventListener('mouseout', () => {
            article_preview_div.classList.remove("border-dark");
            article_preview_div.classList.add('border-light')
            article_preview_div.style.backgroundColor = "inherit";
        });

        article_preview_div.append(title,preview_text, author, pub_date);
        document.getElementById('articles').append(article_preview_div);


    })
}

//removes all "article-preview" objects from the page
function clear_articles_from_page(){
    element = document.getElementsByClassName("article-preview")
    while(element[0]){
        element[0].parentNode.removeChild(element[0]);
    }
}

function load_and_display_one_article(article_id){
    single_article.style.display = "block";
    article_list.style.display = "none";

    hide_paginator(true);
    clear_articles_from_page()

    fetch(`single_article/${article_id}`)
    .then(response => response.json())
    .then(article => {
        document.getElementById('article_title').innerText = article.title;
        document.getElementById('article_body').innerHTML = article.body;
        document.getElementById('article_author').innerText = "By " + article.author;
        document.getElementById('article_pub_date').innerText  ="On " + article.pub_date;
        increment_view_count(article_id);
    });
}

function load_articles(category, page){
    update_vars(category, page);
    hide_paginator(false);

    search_string = "no-search"
    if(search_type === true){
        search_string = search_input.value;
    }

    fetch(`articles/${category}/${page}/${search_string}`)
    .then(response => {
        if(response.status === 404){
            return response.status;
        } else {
            return response.json();
        }
    })
    .then(result => {
        if(result === 404){
            document.getElementById('search_message').innerText = "Couldn't find";
            clear_articles_from_page();

        } else if(1 <= page <= result.number_of_pages){
            document.getElementById('search_message').innerText = "Searching for";
            update_pagination(result.number_of_pages);
            clear_articles_from_page();
            display_articles(result.articles);
        }
    })

}


function increment_view_count(article_id){
    fetch(`/increment_view/${article_id}`)
    .then(response => response.json())
    .then(result => {
        console.log(result)
    })
}

function subscribe(){

    fetch(`/newsletter/`)
    .then(response => response.json())
    .then(result => {
        alert(result.success);
    });

}
