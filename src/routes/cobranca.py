from flask import Blueprint, request, jsonify, Response
import pandas as pd
import os
from datetime import datetime
import urllib.parse
import json

cobranca_bp = Blueprint('cobranca', __name__)

UPLOAD_FOLDER = '/tmp/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@cobranca_bp.route('/upload', methods=['POST'])
def upload_planilha():
    """Upload e processamento da planilha de clientes"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'Nenhum arquivo enviado'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'Nenhum arquivo selecionado'}), 400
        
        # Salvar arquivo temporariamente
        filename = file.filename
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        # Ler planilha
        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            df = pd.read_excel(filepath)
        elif filename.endswith('.csv'):
            df = pd.read_csv(filepath)
        else:
            return jsonify({'error': 'Formato de arquivo não suportado. Use Excel (.xlsx, .xls) ou CSV'}), 400
        
        # Verificar colunas obrigatórias
        required_columns = ['Nome', 'NF', 'Emissão', 'Vencimento', 'Situação', 'Valor', 'Observação']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            return jsonify({
                'error': f'Colunas obrigatórias não encontradas: {", ".join(missing_columns)}',
                'required_columns': required_columns,
                'found_columns': list(df.columns)
            }), 400
        
        # Converter dados para formato JSON
        df['Emissão'] = pd.to_datetime(df['Emissão'], errors='coerce').dt.strftime('%d/%m/%Y')
        df['Vencimento'] = pd.to_datetime(df['Vencimento'], errors='coerce').dt.strftime('%d/%m/%Y')
        df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
        
        # Filtrar apenas registros válidos
        df = df.dropna(subset=['Nome', 'NF'])
        
        df = df.where(pd.notnull(df), None)
        
        data = df.to_dict('records')

        return Response(
            json.dumps({
                'success': True,
                'message': f'Planilha processada com sucesso! {len(data)} registros encontrados.',
                'data': data,
                'total_records': len(data)
            }, ensure_ascii=False),
            mimetype='application/json'
        ) 
        # return jsonify({
        #     'success': True,
        #     'message': f'Planilha processada com sucesso! {len(data)} registros encontrados.',
        #     'data': data,
        #     'total_records': len(data)
        # })
        
    except Exception as e:
        return jsonify({'error': f'Erro ao processar planilha: {str(e)}'}), 500

@cobranca_bp.route('/gerar-email', methods=['POST'])
def gerar_email():
    """Gerar email de cobrança para o Outlook"""
    try:
        data = request.json
        cliente = data.get('cliente', {})
        
        # Template do email
        assunto = f"Cobrança - NF {cliente.get('NF', '')} - {cliente.get('Nome', '')}"
        
        corpo_email = f"""Prezado(a) {cliente.get('Nome', '')},

Espero que esta mensagem o(a) encontre bem.

Estamos entrando em contato para informar sobre a pendência financeira referente à Nota Fiscal nº {cliente.get('NF', '')} com vencimento em {cliente.get('Vencimento', '')}.

Detalhes da cobrança:
• Nota Fiscal: {cliente.get('NF', '')}
• Data de Emissão: {cliente.get('Emissão', '')}
• Data de Vencimento: {cliente.get('Vencimento', '')}
• Valor: R$ {cliente.get('Valor', '0,00')}
• Situação: {cliente.get('Situação', '')}

{cliente.get('Observação', '') if cliente.get('Observação') else ''}

Solicitamos a gentileza de regularizar esta pendência o mais breve possível. Caso já tenha efetuado o pagamento, favor desconsiderar este e-mail e nos enviar o comprovante.

Para esclarecimentos ou negociação, estamos à disposição.

Atenciosamente,
Departamento Financeiro"""
        
        # Criar link mailto para Outlook
        mailto_link = f"mailto:?subject={urllib.parse.quote(assunto)}&body={urllib.parse.quote(corpo_email)}"
        
        return jsonify({
            'success': True,
            'mailto_link': mailto_link,
            'assunto': assunto,
            'corpo': corpo_email
        })
        
    except Exception as e:
        return jsonify({'error': f'Erro ao gerar email: {str(e)}'}), 500

@cobranca_bp.route('/filtrar', methods=['POST'])
def filtrar_dados():
    """Filtrar dados por situação e vencimento"""
    try:
        data = request.json
        registros = data.get('registros', [])
        filtro_situacao = data.get('situacao', '')
        filtro_vencimento = data.get('vencimento', '')
        
        registros_filtrados = registros
        
        # Filtrar por situação
        if filtro_situacao:
            registros_filtrados = [r for r in registros_filtrados if r.get('Situação', '').lower() == filtro_situacao.lower()]
        
        # Filtrar por vencimento (vencidos)
        if filtro_vencimento == 'vencidos':
            hoje = datetime.now().date()
            registros_filtrados = [
                r for r in registros_filtrados 
                if pd.to_datetime(r.get('Vencimento'), format='%d/%m/%Y', errors='coerce').date() < hoje
            ]
        
        return jsonify({
            'success': True,
            'data': registros_filtrados,
            'total_filtrados': len(registros_filtrados)
        })
        
    except Exception as e:
        return jsonify({'error': f'Erro ao filtrar dados: {str(e)}'}), 500

