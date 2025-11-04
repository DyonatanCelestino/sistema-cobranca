# Sistema de Cobrança - Instruções de Instalação

## 📦 Conteúdo do Pacote

Este sistema contém:
- `src/` - Código fonte da aplicação
- `venv/` - Ambiente virtual Python (pré-configurado)
- `requirements.txt` - Lista de dependências
- `exemplo_planilha.csv` - Planilha de exemplo para testes
- `MANUAL_USUARIO.md` - Manual completo de uso
- `README.md` - Este arquivo

## 🚀 Instalação Rápida

### Windows
1. Extraia todos os arquivos para uma pasta (ex: `C:\sistema-cobranca\`)
2. Abra o Prompt de Comando como Administrador
3. Navegue até a pasta: `cd C:\sistema-cobranca`
4. Execute: `venv\Scripts\activate`
5. Execute: `python src\main.py`
6. Abra o navegador em: `http://localhost:5000`

### Linux/Mac
1. Extraia todos os arquivos para uma pasta (ex: `~/sistema-cobranca/`)
2. Abra o Terminal
3. Navegue até a pasta: `cd ~/sistema-cobranca`
4. Execute: `source venv/bin/activate`
5. Execute: `python src/main.py`
6. Abra o navegador em: `http://localhost:5000`

## 🔧 Instalação Manual (se necessário)

Se o ambiente virtual não funcionar, instale manualmente:

```bash
# Criar novo ambiente virtual
python -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar sistema
python src/main.py
```

## 📋 Dependências

O sistema utiliza:
- Flask 3.1.1 - Framework web
- pandas 2.3.0 - Processamento de planilhas
- openpyxl 3.1.5 - Leitura de arquivos Excel
- flask-cors 6.0.0 - Suporte a CORS

## 🧪 Teste Rápido

1. Execute o sistema conforme instruções acima
2. Acesse `http://localhost:5000`
3. Carregue o arquivo `exemplo_planilha.csv` incluído
4. Teste a geração de email clicando em "📧 Email" em qualquer linha

## ⚠️ Requisitos do Sistema

- **Python**: 3.11 ou superior
- **RAM**: Mínimo 512MB disponível
- **Espaço**: 100MB livres
- **Navegador**: Chrome, Firefox, Safari ou Edge (versões recentes)
- **Outlook**: Para geração automática de emails (opcional)

## 🔒 Segurança

- Sistema roda 100% local
- Nenhum dado é enviado para internet
- Arquivos processados temporariamente
- Dados permanecem privados

## 📞 Solução de Problemas

### "Python não encontrado"
- Instale Python 3.11+ do site oficial: https://python.org
- Certifique-se de marcar "Add to PATH" durante instalação

### "Porta 5000 em uso"
- Feche outros programas que possam usar a porta 5000
- Ou edite `src/main.py` e mude `port=5000` para `port=5001`

### "Módulo não encontrado"
- Execute: `pip install -r requirements.txt`
- Certifique-se de estar no ambiente virtual ativado

## 🎯 Próximos Passos

1. Leia o `MANUAL_USUARIO.md` para instruções detalhadas
2. Prepare sua planilha com as colunas obrigatórias
3. Teste com a planilha de exemplo incluída
4. Configure seu Outlook como cliente padrão para melhor experiência

## 📈 Recursos Principais

✅ Upload de planilhas Excel/CSV  
✅ Validação automática de dados  
✅ Interface web moderna e responsiva  
✅ Filtros avançados por situação e vencimento  
✅ Geração automática de emails para Outlook  
✅ Estatísticas em tempo real  
✅ Funcionamento 100% offline  

---

**Desenvolvido para facilitar o gerenciamento de cobranças de forma profissional e eficiente.**

