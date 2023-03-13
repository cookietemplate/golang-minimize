module github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}

require (
	{% if cookiecutter.logger_type == "logrus" -%}github.com/sirupsen/logrus v1.4.1{%- endif %}
	{% if cookiecutter.logger_type == "zap" -%}go.uber.org/zap v1.10.0{%- endif %}
	{% if cookiecutter.use_cobra_cmd == "y" -%}github.com/spf13/cobra v0.0.3{%- endif %}
	{% if cookiecutter.use_viper_config == "y" -%}github.com/spf13/viper v1.3.2{%- endif %}
)

go 1.14
