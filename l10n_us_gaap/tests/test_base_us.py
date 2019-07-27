from odoo.tests.common import TransactionCase
from odoo.tests import tagged


@tagged('post_install', '-at_install')
class TestChartAcount(TransactionCase):

    def test_basic(self):
        chart_us = self.env.ref('l10n_us_gaap.l10n_us_gaap_chart_template')
        chart_us.try_loading_for_current_company()
        bank_account = self.env['account.account'].search(
            [('code', '=', '111101')])
        liquidity_transfer = self.env['account.account'].search([('code', '=', '111901')])
        finished_goods = self.env['account.account'].search([('code', '=', '133000')])
        self.assertEqual(bank_account.name, 'Bank')
        self.assertEqual(liquidity_transfer.name, 'Liquidity Transfer')
        self.assertEqual(finished_goods.name, 'Finished Goods')
