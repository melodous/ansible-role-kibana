import pytest

def test_kibana_server_running_and_enabled(Command,Service):
  # Check that docker service is running and enabled
  docker_service = Service("docker")
  assert docker_service.is_running
  assert docker_service.is_enabled
  # Check that kibana service is running and enabled
  kibana_service = Service("kibana")
  assert kibana_service.is_running
  assert kibana_service.is_enabled

  # Check that kibana-cli ping
  kibana_output = Command.check_output("docker exec kibana kibana-cli ping")
  assert kibana_output == "PONG"

def test_kibana_start_stop(Command,Service):
  Command.run_expect([0],"systemctl stop kibana")
  kibana_service = Service("kibana")
  assert not kibana_service.is_running
  Command.run_expect([0],"systemctl start kibana")
  assert kibana_service.is_running
  Command.run_expect([0],"systemctl restart kibana")
  assert kibana_service.is_running
  kibana_output = Command.check_output("docker exec kibana kibana-cli ping")
  assert kibana_output == "PONG"
