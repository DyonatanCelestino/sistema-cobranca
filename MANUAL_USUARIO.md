# Sistema de Cobrança - Manual do Usuário

## 📋 Visão Geral

O Sistema de Cobrança é uma aplicação web local que permite gerenciar cobranças de clientes através do carregamento de planilhas e geração automática de emails para o Outlook.

## 🚀 Como Instalar e Executar

### Pré-requisitos
- Python 3.11 ou superior
- Navegador web moderno

### Instalação
1. Extraia todos os arquivos do sistema para uma pasta no seu computador
2. Abra o terminal/prompt de comando na pasta do sistema
3. Execute os seguintes comandos:

```bash
# Ativar ambiente virtual
source venv/bin/activate  # No Linux/Mac
# ou
venv\Scripts\activate     # No Windows

# Instalar dependências (se necessário)
pip install -r requirements.txt

# Executar o sistema
python src/main.py
```

4. Abra seu navegador e acesse: `http://localhost:5000`

## 📊 Como Usar

### 1. Preparar a Planilha
Sua planilha deve conter as seguintes colunas obrigatórias:
- **Nome**: Nome do cliente
- **NF**: Número da Nota Fiscal
- **Emissão**: Data de emissão (formato DD/MM/AAAA)
- **Vencimento**: Data de vencimento (formato DD/MM/AAAA)
- **Situação**: Status da cobrança (Pendente, Pago, Vencido)
- **Valor**: Valor da cobrança (formato numérico)
- **Observação**: Observações adicionais

### 2. Carregar a Planilha
1. Na página inicial, clique em "Selecionar Arquivo" ou arraste sua planilha para a área indicada
2. Formatos aceitos: Excel (.xlsx, .xls) ou CSV
3. O sistema processará automaticamente e exibirá os dados

### 3. Visualizar e Filtrar Dados
- **Estatísticas**: Veja resumo com total de clientes, pendentes, vencidos e valor total
- **Filtros**: Filtre por situação (Pendente, Pago, Vencido) ou apenas vencidos
- **Tabela**: Visualize todos os dados organizados

### 4. Gerar Emails de Cobrança
1. Na tabela de dados, clique no botão "📧 Email" ao lado do cliente desejado
2. O sistema gerará automaticamente um email de cobrança personalizado
3. O Outlook será aberto com o email pré-preenchido
4. Revise o conteúdo e envie o email

## 📧 Template do Email

O sistema gera emails com o seguinte formato:

**Assunto**: Cobrança - NF [Número] - [Nome do Cliente]

**Conteúdo**:
- Saudação personalizada
- Detalhes da cobrança (NF, datas, valor, situação)
- Observações específicas do cliente
- Solicitação de regularização
- Assinatura profissional

## 🔧 Funcionalidades

### ✅ Upload de Planilhas
- Suporte a Excel (.xlsx, .xls) e CSV
- Validação automática das colunas obrigatórias
- Processamento de dados com formatação adequada

### ✅ Visualização de Dados
- Interface moderna e responsiva
- Estatísticas em tempo real
- Tabela organizada com status coloridos

### ✅ Filtros Avançados
- Filtrar por situação da cobrança
- Mostrar apenas registros vencidos
- Aplicar múltiplos filtros simultaneamente

### ✅ Geração de Emails
- Templates profissionais personalizados
- Integração direta com Outlook
- Links mailto automáticos

### ✅ Interface Responsiva
- Funciona em desktop e mobile
- Design moderno e intuitivo
- Feedback visual para todas as ações

## 🛠️ Solução de Problemas

### Erro: "Colunas obrigatórias não encontradas"
- Verifique se sua planilha contém todas as colunas obrigatórias
- Certifique-se de que os nomes das colunas estão exatamente como especificado

### Erro: "Formato de arquivo não suportado"
- Use apenas arquivos Excel (.xlsx, .xls) ou CSV
- Verifique se o arquivo não está corrompido

### Email não abre no Outlook
- Certifique-se de que o Outlook está instalado e configurado
- Verifique se o Outlook é o cliente de email padrão do sistema

### Sistema não carrega
- Verifique se o Python está instalado corretamente
- Confirme se todas as dependências foram instaladas
- Verifique se a porta 5000 não está sendo usada por outro programa

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique se seguiu todos os passos de instalação
2. Consulte a seção de solução de problemas
3. Verifique se sua planilha está no formato correto

## 🔒 Segurança

- O sistema roda localmente no seu computador
- Nenhum dado é enviado para servidores externos
- Arquivos são processados temporariamente e removidos após o uso
- Todas as informações permanecem privadas e seguras

