library(rvest)
library(dplyr)
review_link = "https://issuu.com/reviewofreligions"

get_page = function(page){
  sleep = 5
  for(try in 1:5){
    html = read_html(page)
    if(download_okay(html)){
      return(html)
    }
    sleep = sleep * 2
    Sys.sleep(sleep)
  }
  return("I tried - but I failed!")
}

review <- get_page(review_link) |> html_nodes(".sc-4uqco7-1 fzahfw") %>% html_attr('href')


gold_tables <-
  lapply(pages, 
         function(page){ 
           go_link <- paste0(gold_link, "r=", as.character(page))
           gold <- read_html(go_link) |> html_elements(".table-light") |> html_table()
           gold <- gold[[1]]
           header <<-  unlist(gold[1,])
           gold <- gold|>slice(-1)
         }) 

gold_table <- do.call("rbind", gold_tables) 
names(gold_table) <- header