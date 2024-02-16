import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Browser(QMainWindow):
    def __init__(self):
        super(Browser, self).__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        
        # Configurar a página inicial
        self.setGeometry(100, 100, 800, 600)  # Define a posição e o tamanho da janela
        self.show()

        self.setCentralWidget(self.browser)
        self.statusBar()
        # Configurar a barra de navegação
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Voltar', self)
        back_btn.setStatusTip('Voltar para a página anterior')
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Avançar', self)
        forward_btn.setStatusTip('Avançar para a próxima página')
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Recarregar', self)
        reload_btn.setStatusTip('Recarregar página atual')
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Página Inicial', self)
        home_btn.setStatusTip('Ir para a página inicial')
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        navtb = QToolBar("Navegação")
        self.addToolBar(navtb)

        back_btn = QAction('Voltar', self)
        back_btn.setStatusTip('Voltar para a página anterior')
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction('Avançar', self)
        next_btn.setStatusTip('Avançar para a próxima página')
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        navtb.addSeparator()

        home_btn = QAction('Página Inicial', self)
        home_btn.setStatusTip('Ir para a página inicial')
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        stop_btn = QAction('Parar', self)
        stop_btn.setStatusTip('Parar o carregamento da página')
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        search_btn = QAction('Pesquisar', self)
        search_btn.setStatusTip('Pesquisar na web')
        search_btn.triggered.connect(self.search)
        navbar.addAction(search_btn)

        # Configurar a página inicial
        self.show()

        self.setCentralWidget(self.browser)
        self.statusBar()

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    def search(self):
        search_query = self.urlbar.text()
        self.browser.setUrl(QUrl(f"https://www.google.com/search?q={search_query}"))

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def navigate_to_history_entry(self, item):
        url = QUrl.fromUserInput(item.url().toString())
        if url.scheme() == '':
            url.setScheme('http')

        self.browser.setUrl(url)

app = QApplication(sys.argv)
QApplication.setApplicationName("Python Browser")
window = Browser()
app.exec_()
