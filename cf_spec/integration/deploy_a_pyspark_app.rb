require 'spec_helper'

describe 'deploying a PySpark web app' do
  let(:browser)  { Machete::Browser.new(app) }
   let(:app_name) { 'flask_pyspark_web_app' }

  subject(:app)  { Machete.deploy_app(app_name) }

  after { Machete::CF::DeleteApp.new.execute(app) }

  context 'start command is specified in manifest.yml' do
    specify do
      expect(app).to be_running(180)

      browser.visit_path('/')
      expect(browser).to have_body("['i', 'am', 'a', 'string', 'that', 'was', 'sent', 'to', 'spark', 'and', 'back']")
    end
  end
end
