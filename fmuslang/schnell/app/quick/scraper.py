# from schnell.app.appconfig import programming_data
from schnell.app.dirutils import file_under_tempdir, under_tempdir, joiner
from schnell.app.fileutils import file_write
from schnell.app.fmusutils import run_fmus_for_content, run_fmus_for_file
from schnell.app.printutils import indah4
from schnell.app.stringutils import splitstrip
from schnell.app.stringutils import tabify_content_space

sc_provider = {
    '.'     :'colly',
    'c'     :'colly',

    'gq'    :'goquery',

    'b'     :'bs4',
    'j'     :'jsoup',
    's'     :'scrapy',
}

__TEMPLATE_GOQUERY_OUTER = """
doc.Find("__SELECTOR__").Each(func(i int, sel *goquery.Selection) {
    title := strings.TrimSpace(sel.Text())
    content := fmt.Sprintf("%d. %s\\n", i+1, title)
    fmt.Println(content)
})
"""

__TEMPLATE_GOQUERY_OUTER_TEXT_TEXT = """
doc.Find("__SELECTOR__").Each(func(i int, sel *goquery.Selection) {
    first := strings.TrimSpace(sel.Find("__SELECTOR2__").Text())
    second := strings.TrimSpace(sel.Find("__SELECTOR3__").Text())
    formatted := fmt.Sprintf("%d. %s\\n\\t%s\\n\\n", i+1, first, second)
    fmt.Println(formatted)
})
"""

__TEMPLATE_GOQUERY_OUTER_INNER = """
doc.Find("__SELECTOR__").Each(func(i int, sel *goquery.Selection) {
    sel.Find("__SELECTOR2__").Each(func(j int, sel2 *goquery.Selection) {
        content := fmt.Sprintf("%d. %s", j, sel2.Text())
        title := strings.TrimSpace(content)
        fmt.Println(title)
    })
})
"""

__TEMPLATE_COLLY_OUTER_INNER = """
doc.Find("__SELECTOR__").Each(func(i int, sel *goquery.Selection) {
    sel.Find("__SELECTOR2__").Each(func(j int, sel2 *goquery.Selection) {
        content := fmt.Sprintf("%d. %s", j, sel2.Text())
        title := strings.TrimSpace(content)
        fmt.Println(title)
    })
})
// https://benjamincongdon.me/blog/2018/03/01/Scraping-the-Web-in-Golang-with-Colly-and-Goquery/
c.OnHTML("#myCoolSection", func(e *colly.HTMLElement) {
    e.ForEach("p", func(_ int, elem *colly.HTMLElement) {
        if strings.Contains(elem.Text, "golang") {
            fmt.Println(elem.Text)
        }    
    })
})
"""

__TEMPLATE_GOQUERY_OUTER_INNER_INNER = """
doc.Find("__SELECTOR__").Each(func(i int, sel *goquery.Selection) {
    sel.Find("__SELECTOR2__").Each(func(j int, sel2 *goquery.Selection) {
        sel2.Find("__SELECTOR3__").Each(func(k int, sel3 *goquery.Selection) {
            content := fmt.Sprintf("%d. %s", k, sel3.Text())
            title := strings.TrimSpace(content)
            fmt.Println(title)
        })
    })
})
"""

__TEMPLATE_GOQUERY = """
package main

import (
    "fmt"    
    "log"
    "net/http"
    "strings"
    "github.com/PuerkitoBio/goquery"
)

func main() {

    webPage := "__URL__"
    resp, err := http.Get(webPage)

    if err != nil {
        log.Fatal(err)
    }

    defer resp.Body.Close()

    if resp.StatusCode != 200 {
        log.Fatalf("Failed to fetch data from %s: %d %s", webPage, resp.StatusCode, resp.Status)
    }

    doc, err := goquery.NewDocumentFromReader(resp.Body)

    if err != nil {
        log.Fatal(err)
    }

    __OPERATION__
}
"""

__TEMPLATE_COLLY = """
package main
import (
    //"encoding/json"    
    //"io/ioutil"
    //"log"
    //"strconv"
    "fmt"
    "strings"
    //"github.com/gocolly/colly/v2"
    "github.com/gocolly/colly"
    "github.com/gocolly/colly/extensions"
)

func main() {

    data := make([]string, 0)

    c := colly.NewCollector()
    extensions.RandomUserAgent(c)
    extensions.Referer(c)

    c.OnRequest(func(r *colly.Request) {
        r.Headers.Set("Accept", "*/*")
    })

    c.OnHTML("__SELECTOR__", func(e *colly.HTMLElement) {
        __OPERATION__
    })

    c.OnRequest(func(request *colly.Request) {
        fmt.Println("Visiting", request.URL.String())
    })

    c.Visit("__URL__")

    for index, alamat := range data {
        s := fmt.Sprintf("%d: %s", index+1, alamat) + "\\n"
        // s += "\\n"
        fmt.Println(s)
    }
}
"""

__TEMPLATE_COLLY_FMUS = """
__PRC__TEMP__PRC__/__PROJECTNAME__,d(/mk)
    ~if[?!go.mod]
        $* go mod init hapus
        # $* go get github.com/gocolly/colly/v2
        $* go get github.com/gocolly/colly
        $* go get github.com/gocolly/colly/extensions
    $* go run __FILENAME__
"""

__TEMPLATE_GOQUERY_FMUS = """
__PRC__TEMP__PRC__/__PROJECTNAME__,d(/mk)
    ~if[?!go.mod]
        $* go mod init hapus
        $* github.com/PuerkitoBio/goquery
    $* go run __FILENAME__
"""

def scraper(code):
    """
    fm//sc>colly/selection/operasi/object|url
    fm//sc>colly/selection/operasi/object|url

    fm//sc>.article__title/print/text|https://www.scmp.com/
    fm//sc>/.article__title/print/text|https://www.scmp.com/
    fm//sc>colly/.article__title/print/text|https://www.scmp.com/
    fm//sc>colly/.article__title//|https://www.scmp.com/
    no: fm//sc>/.article__title//|https://www.scmp.com/
        colly/selection/operasi/object|url
              selection/operasi/object|url
    """
    left, url = splitstrip(code, '|')
    left_parts = splitstrip(left, '/')
    __PROJECTNAME__ = 'scraping'
    provider = 'colly'
    selection = 'title'
    operasi = 'print'
    obj = 'text'
    res = ''

    print(f'''[scraper.scraper]
    left_parts {left_parts}
    len(left_parts) = {len(left_parts)}
        provider, selection, operasi, obj
                  selection, operasi, obj
                             ^^^^^^^^^^^^dummy
    url {url}
    ''')

    if len(left_parts)==4:
        provider, selection, operasi, obj = left_parts
        provider = sc_provider.get(provider, provider)
    else:
        # provider default = colly
        selection, operasi, obj = left_parts

    if provider == 'colly':
        res = __TEMPLATE_COLLY.replace('__URL__', url)
        res = res.replace('__SELECTOR__', selection)
        # sementara operasi dan obj diabaikan utk print element text...
        # element.Attr("id")
        # activity = 'fmt.Println(strings.TrimSpace(e.Text))'
        activity = 'data = append(data, strings.TrimSpace(e.Text))'
        res = res.replace('__OPERATION__', activity)
    elif provider == 'goquery':
        res = __TEMPLATE_GOQUERY.replace('__URL__', url)
        selector = __TEMPLATE_GOQUERY_OUTER.replace('__SELECTOR__', selection)
        # sementara 1 selection dulu (outer), nanti dukung outer-inner-inner dst
        if '@' in selection:
            '''
            utk SO, dimana kita punya:
            parent      <- search ini
                child   <- print ini
                child   <- dan ini
            fm//sc>gq/.s-post-summary--content@h3@.s-post-summary--content-excerpt//|https://stackoverflow.com/questions/tagged/python
            '''
            if selection.count('@')==2:
                sel1,sel2,sel3 = [item.strip() for item in selection.split('@')]
                selector = __TEMPLATE_GOQUERY_OUTER_TEXT_TEXT.replace('__SELECTOR__', sel1).replace('__SELECTOR2__', sel2).replace('__SELECTOR3__', sel3)
        selector = tabify_content_space(selector)
        res = res.replace('__OPERATION__', selector)
    elif provider == 'scrapy':
        # gunakan hardcoded sementara...
        res = 'scrapy'
    if res:
        indah4(res, warna='green', newline=True)
        projdir = under_tempdir(__PROJECTNAME__)
        if provider == 'colly':
            filename = 'main.go'
            filepath = joiner(projdir, filename)
            file_write(filepath, res)
            fmuscontent = __TEMPLATE_COLLY_FMUS.replace('__FILENAME__', filename).replace('__PROJECTNAME__', __PROJECTNAME__)
            run_fmus_for_content(fmuscontent)
        elif provider == 'goquery':
            filename = 'main.go'
            filepath = joiner(projdir, filename)
            file_write(filepath, res)
            fmuscontent = __TEMPLATE_GOQUERY_FMUS.replace('__FILENAME__', filename).replace('__PROJECTNAME__', __PROJECTNAME__)
            run_fmus_for_content(fmuscontent)
        elif provider == 'scrapy':
            from schnell.app.dirutils import joinhere
            from schnell.app.fileutils import file_content

            scrapyfmus = joinhere(__file__, 'templates/scrapy.fmus')
            scrapyfmuscontent = file_content(scrapyfmus)
            fmuscontent = scrapyfmuscontent.replace('__PROJECTNAME__', __PROJECTNAME__).replace('__URL__', url)

            filename = 'scrapy.fmus'
            filepath = joiner(projdir, filename)
            file_write(filepath, fmuscontent)

            run_fmus_for_file(filepath)
