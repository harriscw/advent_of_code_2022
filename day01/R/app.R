#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(ggplot2)
library(dplyr)
library(plotly)

# Define UI for application that draws a histogram
ui <- fluidPage(
  sidebarLayout(

    sidebarPanel(
  fileInput("file", label = h3("File input")),
  uiOutput("postload")
    ),
  mainPanel(
    tabsetPanel(
      tabPanel("Barplot",plotlyOutput("theplot")),
      tabPanel("Heatmap",plotlyOutput("heatmap"))
    )
    )
  )
  
)

# Define server logic required to draw a histogram
server <- function(input, output) {
  
  theinput <- reactive({
    req(input$file)
    readLines(input$file$datapath)
    # readLines("../input.txt")
    })
  
  bundles=reactive({
    
    req(theinput())
    
    bundles = c()
    acc=0
    for(line in theinput()){ #iterate over each line in input
      if(line != ""){ #if line is not missing then you're still on the same elf...
        acc=acc+as.numeric(line) #...so add value to the running sum
      }else{ #otherwise you've hit the end of the elf... 
        bundles=c(bundles,acc) #...so append to vector of sums per elf
        acc=0 #and reset running sum
      }
    }
    
    bundles
    
  })
  
  output$part1=renderText({
    req(bundles())
    max(bundles())
    
    })
  output$part2=renderText({
    req(bundles())
    sum(tail(sort(bundles()),3))
    })
  
  output$theplot=renderPlotly({
    req(bundles(),input$file)
    
    bundles=bundles()
    
    if(!is.null(input$sort)){
    if(input$sort){
      
      df = data.frame(elf=1:length(bundles),
                      bundle=bundles) %>%
        arrange(-bundle) %>%
        mutate(top=ifelse(row_number() %in% 1:3,"blue","black"))
      
      p=ggplot(data=df, aes(x=as.numeric(reorder(elf,-bundle)), y=bundle, fill=top)) +
        geom_bar(stat="identity") + 
        theme(legend.position = "none") +
        xlab("elf") + labs(caption="Top 3 bundles in blue")
    
    }else{
      
      df = data.frame(elf=1:length(bundles),
                      bundle=bundles) %>%
        mutate(top=ifelse(bundle==max(bundle),"blue","black")) 
      
      p=ggplot(data=df, aes(x=elf, y=bundle,fill=top)) +
        geom_bar(stat="identity") + 
        theme(legend.position = "none") + 
        labs(caption="Top bundle in blue")
      
    }
    ggplotly(p)
    }
    
  })
  
  output$heatmap = renderPlotly({
    
    req(bundles())
    
    bundles=bundles()
    footnote=""
    
    if((length(bundles) %% 10)>0){
      numtoadd=((floor(length(bundles)/10)+1)*10) - length(bundles)
      bundles=c(bundles,rep(0,numtoadd))
      footnote="Elves with bundle values 0 added to make matrix rectangular"
    }
    
    if(!is.null(input$sort)){
      if(input$sort){
        mat = matrix(sort(bundles,decreasing = TRUE),ncol=10)
      }else{
        mat = matrix(bundles,ncol=10)
      }
      
    plot_ly(z = mat, 
            type = "heatmap",
            hoverinfo="text",
            text = mat
            ) %>% 
      layout(xaxis= list(showticklabels = FALSE),
             yaxis= list(showticklabels = FALSE),
             annotations = 
               list(x = 0, y = -.1, 
                    text = footnote, 
                    showarrow = F, 
                    xref='paper', 
                    yref='paper')
             )
    }
    
  })
  
  
  output$postload=renderUI({
    req(bundles(),input$file)
    div(
      p("Part 1:", textOutput(outputId = "part1", inline=T)),
      p("Part 2:", textOutput(outputId = "part2", inline=T)),
      checkboxInput("sort", "Sort Plot", value = FALSE)
    )
  })
  

}

# Run the application 
shinyApp(ui = ui, server = server)
